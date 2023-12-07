from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_user, login_required, logout_user, current_user

from app import db, bcrypt
from app.forms import LoginForm, RegisterForm, PostForm, CommentForm, EditPostForm
from app.models import User, Post, Comment, likes

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html', template='home')


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
    return render_template('login.html', template='login', form=form)


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
    return render_template('register.html', template='register', form=form)


@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def view_all():
    form = PostForm()
    sort = request.args.get('sort', 'date')
    if sort == 'likes':
        posts = Post.query \
            .outerjoin(likes, Post.id == likes.c.post_id) \
            .group_by(Post.id) \
            .order_by(db.func.count(likes.c.post_id).desc(), Post.date_posted.desc()) \
            .limit(10).all()
    else:  # Default sort by date
        posts = Post.query.order_by(Post.date_posted.desc()).limit(10).all()

    # Check which posts the current user has liked
    liked_post_ids = set()
    if current_user.is_authenticated:
        liked_post_ids = {post.id for post in current_user.liked_posts}

    return render_template('dashboard.html', template='dashboard', posts=posts, sort=sort, form=form, liked_post_ids=liked_post_ids)


@main.route('/add_post', methods=['POST'])
@login_required
def add_post():
    form = PostForm()
    new_post = Post(title=form.title.data, content=form.content.data, author=current_user)
    db.session.add(new_post)
    db.session.commit()
    flash('Your post has been created!', 'success')
    return redirect(url_for('main.view_all'))


@main.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post.id).all()
    comment_form = CommentForm()
    edit_post_form = EditPostForm()

    # Check which posts the current user has liked
    liked_post_ids = set()
    if current_user.is_authenticated:
        liked_post_ids = {post.id for post in current_user.liked_posts}

    return render_template('view_post.html', template='view_post', post=post, comments=comments, comment_form=comment_form, edit_post_form=edit_post_form, liked_post_ids=liked_post_ids)


@main.route('/like_post/<int:post_id>', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user in post.likers:
        post.likers.remove(current_user)
        db.session.commit()
        return jsonify({'result': 'unliked', 'likes_count': len(post.likers)})
    else:
        post.likers.append(current_user)
        db.session.commit()
        return jsonify({'result': 'liked', 'likes_count': len(post.likers)})


@main.route('/add_comment/<int:post_id>', methods=['POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = Comment(content=comment_form.content.data, post_id=post.id, author=current_user)
        db.session.add(comment)
        db.session.commit()
    else:
        flash('Error adding comment.', 'error')

    return redirect(url_for('main.view_post', post_id=post.id))


@main.route('/delete_comment/<int:comment_id>', methods=['DELETE'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Check if the current user is authorized to delete the comment
    if current_user != comment.author:
        return jsonify({'message': 'Unauthorized'}), 403

    db.session.delete(comment)
    db.session.commit()
    return jsonify({'message': 'Comment deleted'})


@main.route('/edit_comment/<int:comment_id>', methods=['POST'])
@login_required
def edit_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Check if the current user is authorized to edit the comment
    if current_user != comment.author:
        return jsonify({'message': 'Unauthorized'}), 403

    data = request.json
    comment.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Comment updated'})


@main.route('/update_post/<int:post_id>', methods=['POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Check if the current user is authorized to edit the post
    if current_user != post.author and not current_user.is_admin:
        return jsonify({'message': 'Unauthorized'}), 403

    post.title = request.form.get('title')
    post.content = request.form.get('content')
    db.session.commit()
    flash('Post updated', 'success')
    return redirect(url_for('main.view_all'))


@main.route('/delete_post/<int:post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Check if the current user is authorized to edit the post
    if current_user != post.author:
        return jsonify({'message': 'Unauthorized'}), 403

    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', 'success')
    return jsonify({'message': 'Post deleted'})
