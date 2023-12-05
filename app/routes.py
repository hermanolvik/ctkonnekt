from flask import Blueprint, render_template, redirect, url_for, flash
from sqlalchemy import func

from app.forms import LoginForm, RegisterForm, PostForm, CommentForm
from app.models import User, Post, Comment
from app import db, bcrypt
from flask_login import login_user, login_required, logout_user, current_user
from flask import request

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main.view_all'))
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)


@main.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already registered. Please log in or use a different email.', 'warning')
            return redirect(url_for('main.register'))

        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(
            email=form.email.data,
            password=hashed_password,
            first_name=form.first_name.data,
            family_name=form.family_name.data
        )
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def view_all():
    form = PostForm()

    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.view_all'))

    sort = request.args.get('sort', 'date')  # Default sort by date

    if sort == 'likes':
        posts = Post.query.outerjoin(Post.likers).group_by(Post.id) \
            .order_by(func.count(Post.likers).desc(), Post.date_posted.desc()).limit(10).all()
    else:  # Default sort by date
        posts = Post.query.order_by(Post.date_posted.desc()).limit(10).all()

    return render_template('dashboard.html', template='dashboard', posts=posts, sort=sort, form=form)


@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post.id).all()
    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(content=form.content.data, post_id=post.id, author=current_user)
        db.session.add(comment)
        db.session.commit()
        flash('Your comment has been posted.', 'success')
        return redirect(url_for('main.view_post', post_id=post.id))

    return render_template('view_post.html', post=post, comments=comments, form=form)