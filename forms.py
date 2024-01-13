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
        ('/static/assets/img/profile_pictures/astronaut.jpg', 'Astronaut'), 
        ('/static/assets/img/profile_pictures/astro_female.jpg', 'Female Astronaut'),
        ('/static/assets/img/profile_pictures/astro_king.jpg', 'King'),
        ('/static/assets/img/profile_pictures/astro_cesar.jpg', 'Cesar'),
        ('/static/assets/img/profile_pictures/astro_cowboy.jpg', 'Cowboy'),
        ('/static/assets/img/profile_pictures/astro_pirat.jpg', 'Pirat'),
        ('/static/assets/img/profile_pictures/astro_warrior.jpg', 'Warrior'),
        ('/static/assets/img/profile_pictures/astro_samurai.jpg', 'Samurai'),
        ('/static/assets/img/profile_pictures/astro_wizard.jpg', 'Wizard'),
        ('/static/assets/img/profile_pictures/astro_witch.jpg', 'Witch'),
        ('/static/assets/img/profile_pictures/astro_devil.jpg', 'Devil'),
        ('/static/assets/img/profile_pictures/astro_reaper.jpg', 'Reaper'),
        ('/static/assets/img/profile_pictures/astro_koala.jpg', 'Koala'),
        ('/static/assets/img/profile_pictures/astro_fox.jpg', 'Fox'),
        ('/static/assets/img/profile_pictures/astro_panda.jpg', 'Panda'),
    ])
    submit = SubmitField('Save Changes')
