from datetime import date, datetime
from flask import Flask, abort, jsonify, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship, joinedload
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm, EditProfileForm




app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)

# FLASK_LOGIN CONFIG
login_manager = LoginManager()
login_manager.init_app(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50))
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")
    profile_picture = db.Column(db.String(255), default="/static/assets/img/avatars/default-profile.jpg")
    when_joined = db.Column(db.DateTime, default=datetime.utcnow)
    bio = db.Column(db.String(50))
    location = db.Column(db.String(50))
    likes = relationship("Like", back_populates="users")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    post_comments = relationship("Comment", back_populates="parent_post")
    

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="post_comments")
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    likes_count = db.Column(db.Integer, default=0)
    likes = relationship("Like", back_populates="comments")


class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"))
    users = relationship("User", back_populates="likes")
    comments = relationship("Comment", back_populates="likes")



with app.app_context():
    db.create_all()


# Admin only decorator
def admin_only(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_func


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)



# Register route
@app.route('/register', methods=["GET", "POST"])
def register():

    form = RegisterForm()
    if form.validate_on_submit():

        result = db.session.execute(db.select(User).where(User.email==form.email.data))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead", "danger")
            return redirect(url_for('login'))

        # Password hashing and salting
        hash_and_salted_pass = generate_password_hash(
            form.password.data,
            method="pbkdf2:sha256",
            salt_length=10
        )

        new_user = User(
            email = form.email.data,
            name = form.name.data,
            password = hash_and_salted_pass
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html", form=form)




# Login route
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        result = db.session.execute(db.select(User).where(User.email==email))
        user = result.scalar()

        if not user:
            flash("This email does not exist, please try again", "danger")
            return redirect(url_for("login"))
        
        elif not check_password_hash(user.password, password):
            flash("Incorrect password, please try again", "danger")
    
        else:
            login_user(user)
            flash("Logged in successfully", "success")
            return redirect(url_for("get_all_posts"))

    return render_template("login.html", form=form, current_user=current_user)


# Logout route
@app.route('/logout')
def logout():
    logout_user()
    flash("Signed out", "warning")
    return redirect(url_for('get_all_posts'))


# Home/index route
@app.route('/')
def get_all_posts():
    page = request.args.get("page", 1, type=int)
    posts = BlogPost.query.paginate(page=page, per_page=3)
    return render_template("index.html", all_posts=posts)


# Post route with comment form
@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)

    comment_form = CommentForm()

    # Only allow logged-in users to comment on posts
    if comment_form.validate_on_submit():
        if not current_user.is_authenticated:
            flash("You need to login or register to comment", "danger")
            return redirect(url_for("login"))

        new_comment = Comment(
            text=comment_form.comment_text.data,
            comment_author=current_user,
            parent_post=requested_post
        )
        db.session.add(new_comment)
        db.session.commit()

    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form)


# Add new post route with decorator so only an admin user can create a new post
@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


# Edit post route with decorator so only an admin user can edit a post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


# Delete post route, only admin can delete a post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Comment delete route, only comment author or admin/moderator can delete a comment
@app.route("/delete_comment/<int:comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.options(joinedload(Comment.parent_post)).get(comment_id)

    # Check if the current user is the comment author or an admin
    if current_user.id == comment.comment_author.id or current_user.id == 1:
        post_id = comment.parent_post.id
        db.session.delete(comment)
        db.session.commit()
        flash("Comment deleted successfully", "success")
    else:
        flash("You don't have permission to delete this comment", "danger")
        post_id = None

    return redirect(url_for("show_post", post_id=post_id))



# User profile page route
@app.route('/profile')
@login_required
def profile():
    return render_template('user-page.html')



# Like route. Each user can like one comment once
@app.route('/like_comment/<comment_id>', methods=['GET'])
@login_required
def like_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    like = Like.query.filter_by(author_id=current_user.id, comment_id=comment_id).first()

    if not comment:
        flash("comment does not exist", "warning")
    elif like:
        db.session.delete(like)
        db.session.commit()
    else:
        like = Like(author_id=current_user.id, comment_id=comment_id)
        db.session.add(like)
        db.session.commit()

    return redirect(url_for('show_post', post_id=comment.parent_post.id))



# User setting route
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    
    form = EditProfileForm()

    if form.validate_on_submit():
        new_username = form.username.data
        new_email = form.email.data
        new_password = form.password.data
        new_profile_picture = form.profile_picture.data
        new_location = form.location.data
        new_bio = form.bio.data

        # Update data only if different
        if new_username and new_username != current_user.name:
            current_user.name = new_username
        
        # Checking if new email field is not empty
        if new_email and new_email != current_user.email:
            current_user.email = new_email


        # Checking if new location field is not empty
        if new_location != current_user.location:
            current_user.location = new_location


        # Checking if new bio field is not empty
        if new_bio != current_user.bio:
            current_user.bio = new_bio


        if new_password:
            # Password hashing
            hashed_password = generate_password_hash(
                new_password,
                method="pbkdf2:sha256",
                salt_length=8
            )
            current_user.password = hashed_password

        if new_profile_picture and new_profile_picture != current_user.profile_picture:
            current_user.profile_picture = new_profile_picture

        if 'cancel' in request.form:
            pass 
        else:
            db.session.commit()
            flash('Profile updated successfully', 'success')

        return redirect(url_for('settings'))

    return render_template('user-settings.html', form=form)



# Route to view profile-page of another user
@app.route('/user/id=<int:user_id>')
def view_user_profile(user_id):
    user = db.get_or_404(User, user_id)
    return render_template('view-user-profile.html', user=user)


# About page route
@app.route("/about")
def about():
    return render_template("about.html")


# Contact page route
@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run(debug=True, port=5002)
