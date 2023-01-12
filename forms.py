from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Email, Length, URL


class SignupForm(FlaskForm):
    username = StringField("username", validators=[InputRequired(),
                                                   Length(min=4, max=30, message="Min 4 characters and max 30")])
    email = StringField("email", validators=[InputRequired(),
                                             Email(message='Not a valid email')])
    password = PasswordField("password", validators=[InputRequired(),
                                                     Length(min=6, message='Password must be at least 6 characters')])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):

    email = StringField("email", validators=[InputRequired(),
                                             Email(message='Not a valid email')])
    password = PasswordField("password", validators=[InputRequired(),
                                                     Length(min=4, message='Password must be at least 6 characters')])
    remember = BooleanField('Remember me')
    submit = SubmitField("Sign In")


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
