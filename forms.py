from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, SelectField, TextAreaField
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
    submit = SubmitField("Sign me up")



class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log me in")



class CommentForm(FlaskForm):
    comment_text = TextAreaField("Add comment", validators=[DataRequired()])
    submit = SubmitField("Post")



class EditProfileForm(FlaskForm):
    username = StringField('Username')
    email = EmailField('Email')
    password = PasswordField('New password', render_kw={"placeholder": "••••••••"})
    bio = StringField('Bio', render_kw={"placeholder": "Add"})
    location = StringField('Location', render_kw={"placeholder": "Add"})
    profile_picture = SelectField('Profile Picture', choices=[
        ('/static/assets/img/avatars/default-profile.jpg', 'None'), 
        ('/static/assets/img/avatars/man_1.png', 'Man 1'),
        ('/static/assets/img/avatars/man_2.png', 'Man 2'),
        ('/static/assets/img/avatars/man_3.png', 'Man 3'),
        ('/static/assets/img/avatars/man_4.png', 'Man 4'),
        ('/static/assets/img/avatars/man_5.png', 'Man 5'),
        ('/static/assets/img/avatars/man_6.png', 'Man 6'),
        ('/static/assets/img/avatars/man_7.png', 'Man 7'),
        ('/static/assets/img/avatars/man_8.png', 'Man 8'),
        ('/static/assets/img/avatars/man_9.png', 'Man 9'),
        ('/static/assets/img/avatars/man_10.png', 'Man 10'),
        ('/static/assets/img/avatars/woman_1.png', 'Woman 1'),
        ('/static/assets/img/avatars/woman_2.png', 'Woman 2'),
        ('/static/assets/img/avatars/woman_3.png', 'Woman 3'),
        ('/static/assets/img/avatars/woman_4.png', 'Woman 4'),
        ('/static/assets/img/avatars/woman_5.png', 'Woman 5'),
        ('/static/assets/img/avatars/woman_6.png', 'Woman 6'),
        ('/static/assets/img/avatars/woman_7.png', 'Woman 7'),
        ('/static/assets/img/avatars/woman_8.png', 'Woman 8'),
        ('/static/assets/img/avatars/woman_9.png', 'Woman 9'),
        ('/static/assets/img/avatars/woman_10.png', 'Woman 10'),
    ], render_kw={"placeholder": '{{ current_user.profile_picture }}' })
    submit = SubmitField('Save Changes')


    def set_default_username(self, username):
        self.username.default = username
        self.process()


    def set_default_email(self, email):
        self.email.default = email
        self.process()


    def set_default_profile_picture(self, user_profile_picture):
        self.profile_picture.default = user_profile_picture
        self.process()


    def set_default_location(self, user_location):
        self.location.default = user_location
        self.process()

    def set_default_bio(self, user_bio):
        self.bio.default = user_bio
        self.process()

