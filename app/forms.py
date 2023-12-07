from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import Length, InputRequired, ValidationError, DataRequired
from app.models import User


class RegisterForm(FlaskForm):
    first_name = StringField(validators=[InputRequired(), Length(
        max=50)], render_kw={"placeholder": "First Name"})
    family_name = StringField(validators=[InputRequired(), Length(
        max=50)], render_kw={"placeholder": "Family Name"})
    email = StringField(validators=[InputRequired(), Length(
        min=4, max=120)], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)],
                             render_kw={"placeholder": "Password"})
    confirm_password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)],
                                     render_kw={"placeholder": "Confirm Password"})
    submit = SubmitField("Register")

    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError('That email already exists. Please choose a different one.')

    def validate_confirm_password(self, confirm_password):
        if confirm_password.data != self.password.data:
            raise ValidationError('Passwords must match.')


class LoginForm(FlaskForm):
    email = StringField(validators=[
        InputRequired(), Length(min=4, max=120)], render_kw={"placeholder": "Email"})

    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])


class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Post Comment')


class EditPostForm(FlaskForm):
    post_id = HiddenField('Post ID')
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
