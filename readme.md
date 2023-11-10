# User Review System - GitHub Repository README

## Introduction

This GitHub repository contains the code for a User Review System, implemented in Python using the Bottle web framework and PyMongo for MongoDB integration. The system allows users to create accounts, log in, submit reviews, and view their reviews on a dashboard. This README provides an overview of the code and its functionality.

# Documentation

Our `docs` directory in the repository contains various documents that provide more insight into our project. Here's a guide to help you navigate through them:

- **assignment1.md**: Contains the details about the first assignment related to our project, including specifications and evaluation criteria.
- **attribution_template.md**: A template for attributing work and contributions to the project by team members or third parties.
- **code_review.md**: Outlines our code review process, standards, and checklists to ensure quality and consistency in our codebase.
- **meetingNotes.md**: Notes from our team meetings, capturing the key points discussed, decisions made, and action items.
- **project_description.md**: An in-depth description of the project, including its scope, objectives, and intended outcomes.
- **source-control_str.md**: Describes our strategy for source control, including branch naming conventions, merge strategies, and commit policies.
- **team_reviews.md**: Documentation of peer reviews within the team, reflecting on the work done and providing feedback for improvement.
- **user_stories.md**: A collection of user stories that guide the development of the project, ensuring we're building features that users actually need.

Please refer to each document for detailed information on its respective topic.

# Views Directory

The `views` directory contains template files that define the structure and layout of the web pages in our application. Below is a description of each file and its purpose:

- **create_review.tpl**: Template for the page where users can create new reviews.
- **dashboard.tpl**: The main dashboard view that users see after logging in, which provides an overview of their activity and options.
- **edit_review.tpl**: A form view that allows users to edit their existing reviews.
- **homepage.tpl**: The landing page of our website, showcasing the main features and entry points into the application.
- **login.tpl**: The login page template where users can enter their credentials to access their accounts.
- **profile.tpl**: Displays the user profile where personal information and user-specific data are shown.
- **reviews.tpl**: This template is used to display a list of reviews, allowing users to browse through different submissions.
- **search_results.tpl**: Shows the results of a user's search query, formatted for easy reading and navigation.
- **signup.tpl**: The sign-up page template where new users can register for an account.
- **view_review.tpl**: A detailed view of a single review, including options to like, dislike, and comment.

Each template is designed to be responsive and user-friendly, ensuring a seamless experience across various devices and screen sizes.

# Server

The server.py contains all the backend code for the website. 
## Running the Server
To start the server, run the following command from the root of the project directory:
python server.py
The server will start, and the application will be accessible at http://localhost:8080/ by default.
Once the server is running, you should be able to access the dashboard and other pages via your web browser at `http://localhost:8080/dashboard` or whichever port you have configured.

## (Zawad)
## Available Routes for the dashboard
The server handles the following routes:
### functions
- `/dashboard`: Displays the dashboard with user reviews.
- `/edit_review/<review_id>`: Opens a review for editing.
- `/update_review`: Endpoint for submitting the updated review.
- `/delete_review/<review_id>`: Endpoint for deleting a review.
- `/create_review`: Displays a form to create a new review.
- `/store_review`: Endpoint for storing the new review.
- `/like_review/<review_id>`: Endpoint for liking or disliking a review.
### Unit tests 
Unit tests for the functions

## (Mahad)

In this section, I'll outline the specific code contributions and relevant docstrings for my part of the project. I've 
primarily worked on the user authentication and session management aspects of the codebase.

#### `server.py`

In the `server.py` script, I've added the following routes and functions related to user authentication and registration:

- `/login` (POST): This route handles user login. It retrieves the username and password from the request form, attempts
 to authenticate the user, and creates a new session upon successful login.
  - Relevant function: `do_login()`

- `/profile`: This route displays the user's profile if a valid session exists, or redirects to the login page if no valid session exists.
  - Relevant function: `profile()`

- `/signup` (POST): This route is responsible for user registration (sign-up). It parses user registration data, checks 
 for duplicate usernames, generates a unique user ID, and inserts the new user into the 'users_collection'.
  - Relevant function: `do_signup()`

### Database Configuration

I've played a key role in configuring the MongoDB database for our project, including defining the database structure, collections, and connections.

#### `server.py`

In the `server.py` script, I've established the following MongoDB collections and integrated them into our project:

- `users_collection`: This collection stores user information, such as user IDs, names, usernames, email addresses, and hashed passwords (for security).
- `sessions_collection`: It is responsible for managing user sessions, storing session data, and ensuring secure authentication.
- `reviews_collection`: This collection holds user reviews, including information such as review content, user IDs, timestamps, and likes/dislikes.
- `comments_collection`: For comments on reviews, this collection stores data about review IDs, usernames, and comment content.

I've ensured that the collections are appropriately set up and ready to store and retrieve data for their respective purposes.

### MongoDB Integration

I've integrated the MongoDB database into our project, allowing data storage, retrieval, and manipulation:

- For user registration and authentication, I've implemented functions to insert and retrieve user data from the `users_collection`.
- For session management, I've utilized the `sessions_collection` to securely manage user sessions.
- When users create reviews, the `reviews_collection` stores review data, while comments on reviews are stored in the `comments_collection`.

This database setup and integration ensure that our project can effectively manage user accounts, sessions, reviews, and comments, providing a seamless experience for users.
### Commenting on Reviews

I've implemented the functionality to add comments to reviews specified by their unique IDs. This allows users to engage in discussions and provide feedback on reviews.
I've added the following route and functions for commenting on reviews in the `server.py` script:

- `/add_comment/<review_id>` (GET and POST): This route handles the addition of comments to a review identified by its unique ID.
  - Relevant function: `comment(review_id)`

If the request method is POST, the function retrieves the comment content from the request form, associates it with the user's username, and inserts it into the `comments_collection`. Subsequently, the user is redirected to the review view.
If the request method is GET, the function is responsible for displaying comments associated with the review. It retrieves the review and its associated comments from the database and renders them using a template.
This feature enhances user engagement and interaction within the review system, allowing users to provide valuable feedback and insights on reviews.

### Code Documentation

In addition to the code contributions, I've also added docstrings and explanations within the code to make it more understandable 
and maintainable. Clear and concise documentation is crucial for the success of our project.

I'll continue to actively work on these features, collaborate with the team, and ensure that the codebase remains well-documented and functional.

## (Dayeem)

## (Jason)


# Session Management

The `server.py` script includes a session management system that provides secure user authentication and session handling 
using cookies and MongoDB for storage.The session ID is stored securely as a cookie in the user's browser.

## Overview

The session management is facilitated through several key functions:

- `create_session`: Generates a unique session ID and stores user session data in MongoDB and a local dictionary.
- `delete_session`: Deletes a user session from MongoDB and the local storage based on the session ID.
- `manage_sessions`: Acts as a hook to manage user sessions before processing requests.
- `get_session`: Retrieves the current user session data from a request.

## Setup

Ensure MongoDB is running and a `sessions_collection` is created to store session data.

## Usage

### Creating Sessions
When a user logs in, call `create_session` with the user's details to initiate a session.
Example:
session_id = create_session(user_id, username, password, first_name, last_name, email, sessions_collection)
response.set_cookie('session_id', session_id)

### Deleting Sessions
To log out a user, invoke delete_session with the user's session ID.
Example:
delete_session(session_id, sessions_collection)
response.delete_cookie('session_id')

### Managing Sessions
Incorporate manage_sessions as a hook or middleware in your application to validate sessions on each request.
Example:
@app.hook('before_request')
def before_request():
    manage_sessions(sessions_collection)

### Retrieving Sessions
Use get_session to access the session data in the context of a request.
Example:
session_data = get_session(request)


# User Registration and Authentication

The `user_info.py` script contains functions to register new users and authenticate existing ones against credentials stored in a MongoDB database.

## Overview

This script provides two primary functions:

- `register_user`: Registers a new user in the database.
- `authenticate_user`: Authenticates a user's login attempt.

## Usage

### Registering Users
To register a new user, call register_user with the required personal information.
Example:
message = register_user('John', 'Doe', 'johndoe', 'john@example.com', 'password123')
print(message)

### Authenticating Users
To authenticate a user, call authenticate_user with the username and password.
Example:
is_authenticated = authenticate_user('johndoe', 'password123')
if is_authenticated:
    print("Login successful.")
else:
    print("Login failed.")


    