from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, SelectField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField



class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")



class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign me up.")




class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log me in.")



class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit")


class EditProfileForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('Email')
    password = PasswordField('Password')
    profile_picture = SelectField('Profile Picture', choices=[
        ('/static/images/profile_pictures/astronaut.jpg', 'Astronaut'), 
        ('/static/images/profile_pictures/astro_female.jpg', 'Female Astronaut'),
        ('/static/images/profile_pictures/astro_king.jpg', 'King'),
        ('/static/images/profile_pictures/astro_cesar.jpg', 'Cesar'),
        ('/static/images/profile_pictures/astro_cowboy.jpg', 'Cowboy'),
        ('/static/images/profile_pictures/astro_pirat.jpg', 'Pirat'),
        ('/static/images/profile_pictures/astro_warrior.jpg', 'Warrior'),
        ('/static/images/profile_pictures/astro_samurai.jpg', 'Samurai'),
        ('/static/images/profile_pictures/astro_wizard.jpg', 'Wizard'),
        ('/static/images/profile_pictures/astro_witch.jpg', 'Witch'),
        ('/static/images/profile_pictures/astro_devil.jpg', 'Devil'),
        ('/static/images/profile_pictures/astro_reaper.jpg', 'Reaper'),
        ('/static/images/profile_pictures/astro_koala.jpg', 'Koala'),
        ('/static/images/profile_pictures/astro_fox.jpg', 'Fox'),
        ('/static/images/profile_pictures/astro_panda.jpg', 'Panda'),
    ])
    submit = SubmitField('Save Changes')
