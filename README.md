# Project Documentation

## Table of Contents

1. [Introduction](#introduction)
2. [Project Structure](#project-structure)
3. [Dependencies](#dependencies)
4. [Getting Started](#getting-started)
5. [Features](#features)
   1. [Theme Toggle](#theme-toggle)
   2. [Profile Section](#profile-section)
      1. [Editing Profile](#editing-profile)
      2. [Avatar Selection](#avatar-selection)
      3. [Profile Bio](#profile-bio)
   4. [Deleting Comments](#deleting-comments)
   5. [Commenting on Posts](#commenting-on-posts)
   6. [Admin and Moderator Roles](#admin-and-moderator-roles)
   7. [Post Management by Admin](#post-management-by-admin)
   8. [Like Functionality for Comments](#like-functionality-for-comments)
   9. [Pagination](#pagination)
6. [What I Learned](#what-i-learned)

---

## Introduction<a name="introduction"></a>

This project is a blog platform with various posts, built using [Bootstrap 5](https://getbootstrap.com/) and [Flask](https://flask.palletsprojects.com/) for the backend. It provides a dynamic space for discussions and content sharing. 
It serves as a user profile display and management system with additional features such as theme toggling, comment functionality, and user roles.

---

## Project Structure<a name="project-structure"></a>

The project follows a standard Flask application structure. Key directories and files include:
- **templates**: HTML templates for rendering pages.
- **static**: Static files such as images and stylesheets.
- **app.py**: Main Flask application file.
- **README.md**: Project documentation.

---

## Dependencies<a name="dependencies"></a>

The project relies on the following technologies and libraries:
- [Bootstrap 5](https://getbootstrap.com/)
- [Flask](https://flask.palletsprojects.com/)

---

## Getting Started<a name="getting-started"></a>

To run the project locally, follow these steps:

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application with `python app.py`.
4. Access the application in your web browser at `http://localhost:5000`.

---

## Features<a name="features"></a>

### Theme Toggle<a name="theme-toggle"></a>

The project includes a theme toggle functionality that allows users to switch between light and dark themes. The theme is automatically set based on the user's system preference, but users can manually toggle it as well.


### Profile Section<a name="profile-section"></a>

The main profile section displays user information, including a profile picture, name, role, join date, comment count, email, and location (if available). User roles are color-coded (Admin: yellow, Moderator: purple, User: blue).

   ####    Editing Profile<a name="editing-profile"></a>

Users can edit their profiles in profile settings page. This reveals a form for updating profile details.

   ####    Avatar Selection<a name="avatar-selection"></a>

Users can select their profile picture from a predefined list of avatars. The avatar selection is facilitated through the `updateSelectedAvatar` JavaScript function.

   ####    Profile Bio<a name="profile-bio"></a>

Users can provide a bio that is displayed in the profile section. If no bio is provided, a placeholder message encourages users to share something about themselves.



### Deleting Comments with confirmation modal<a name="deleting-comments-with-confirmation-modal"></a>

The application utilizes jQuery to handle the deletion of comments. When a user or admin attempts to delete a comment, a confirmation modal pops up to ensure that the action is intentional, preventing accidental deletions.



### Commenting on Posts<a name="commenting-on-posts"></a>

Users have the ability to add comments to posts. Each post can have multiple comments, and users can express their thoughts or ask questions by participating in the comment section.



### Admin and Moderator Roles<a name="admin-and-moderator-roles"></a>

The application supports different user roles, including Admin and Moderator. Admin users have the privilege to add new posts, edit existing posts, and delete comments from all users. Moderators, on the other hand, can delete comments from other users.



### Like Functionality for Comments<a name="like-functionality-for-comments"></a>

Users can express appreciation for comments by liking them. This adds a positive engagement aspect to the platform, allowing users to show support for valuable or interesting contributions.



### Pagination<a name="pagination"></a>

The pagination functionality in the index.html file enables users to navigate through a list of blog posts more efficiently.

---

## What I Learned<a name="what-i-learned"></a>

Throughout the development of this project, I gained valuable experience in the following areas:

- **Flask Framework**: Understanding and implementing a web application using the Flask framework for the backend.
- **Bootstrap 5**: Utilizing Bootstrap 5 for responsive and visually appealing frontend design.
- **User Authentication and Roles**: Implementing user authentication and defining different roles (Admin, Moderator, User) with specific privileges.
- **JavaScript and jQuery**: Incorporating client-side interactivity, such as avatar selection and theme toggling, using JavaScript and jQuery.
- **Database Management**: Handling user data and post-related information within the application's database.
- **Commenting and Like Functionality**: Implementing a commenting system for posts and allowing users to like comments to encourage user engagement.
- **Project Documentation**: Creating comprehensive and organized project documentation for clarity and ease of understanding.

These skills contribute to a well-rounded understanding of web development and form a solid foundation for future projects and enhancements.


#### Feel free to explore the codebase and enhance the project further! If you encounter any issues or have suggestions, please open an issue on GitHub. Contributions are welcome!
