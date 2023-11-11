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

- Unit tests for the functions
**Unit Tests:** Run by `python -m unittest test_server` in terminal.


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



## (Jason)
### Here are my tasks for sprint 2 and where to find them:

1. **Updating HTML templates for session management:**
   - **Files:** `dashboard.tpl`, `profile.tpl`
   - **Description:** In this task, I updated the HTML templates for session management. This enhancement ensures that users have a personalized experience based on their profile information. The session management feature allows the server to identify and remember users, providing a customized dashboard and profile view.
   - You can exercise this code by checking the `/dashboard` and `/profile` pages.

2. **Designing and coding the HTML form for comments and displaying comments:**
   - **File:** `view_review.tpl`
   - **Description:** This task involved designing and coding the HTML form responsible for handling user comments. Additionally, I implemented the display functionality to show existing comments on the review page (`view_review.tpl`). Users can submit comments through the form, and the comments are dynamically displayed on the same page.
   - You can exercise this by using the `/view_review` page and type a comment.

3. **Designing and coding the HTML form for like/dislike and displaying the count of likes/dislikes:**
   - **File:** `view_review.tpl`
   - **Description:** I created the HTML form to handle user interactions for liking or disliking a review. The count of likes and dislikes is displayed on the review page (`view_review.tpl`). This feature allows users to express their opinion on a review and see the overall popularity of the review based on the accumulated likes and dislikes.
   - You can exercise this by using the `/view_review` page and click the like or dislike button.

4. **Designing and coding the HTML form for the search bar:**
   - **File:** `reviews.tpl`
   - **Description:** For this task, I designed and implemented the HTML form for the search bar. Users can input search queries to find specific reviews. The search functionality enhances user experience by allowing them to quickly locate reviews based on relevant keywords or phrases.
   - You can exercise this by using the `/reviews` page and using the search bar.

5. **Designing and coding the HTML form for the rating review:**
   - **File:** `view_review.tpl`
   - **Description:** I implemented the HTML form for users to provide a rating for a particular review. This feature allows users to express their opinion on the quality of a review by assigning a numerical rating. The rating form is displayed on the review page (`view_review.tpl`).
   - You can exercise this by using the `/view_reviews` page and rate the review.

6. **Completing the process model document:**
   - **File:** `process_model.md`
   - **Description:** This task involved completing the process model document (`process_model.md`). The document outlines the workflow and processes involved in the system. It serves as a comprehensive guide to understand how different components of the application interact and function together.

**Unit Tests:** Run by `python -m unittest test_server` in terminal.

## (Md Golam Mahmud - Dayeem)

## Session Management

The `server.py` script includes a session management system that provides secure user authentication and session handling implemented in a `session_management.py`
using cookies and MongoDB for storage.The session ID is stored securely as a cookie in the user's browser. The `session_management.py` is imported in the `server.py` to create sessions while doing a login.

### Overview

The session management is facilitated through several key functions:

- `create_session`: Generates a unique session ID and stores user session data in MongoDB and a local dictionary.
This method is called in the `do_login` method in the `server.py` 
- `delete_session`: Deletes a user session from MongoDB and the local storage based on the session ID.
This is called in the `logout` method to delete sessions when the user logs out.
- `manage_sessions`: Acts as a hook to manage user sessions before processing requests.
This is called in the `session_manager` method in `server.py`
- `get_session`: Retrieves the current user session data from a request.
This is called `profile` method in the `server.py`

### Setup

Ensure MongoDB is running and a `sessions_collection` is created to store session data.

### Usage

### Creating Sessions
When a user logs in, call `create_session` with the user's details to initiate a session.
Example:
session_id = create_session(user_id, username, password, first_name, last_name, email, sessions_collection)
response.set_cookie('session_id', session_id)

### Deleting Sessions
When a user logs out, `delete_session` function is invoked with the user's session ID.
Example:
delete_session(session_id, sessions_collection)
response.delete_cookie('session_id')

### Managing Sessions
Incorporated manage_sessions as a hook or middleware in your application to validate sessions on each request.
Example:
@app.hook('before_request')
def before_request():
    manage_sessions(sessions_collection)

### Retrieving Sessions
Using `get_session` to access the session data in the context of a request.
Example:
session_data = get_session(request)

### Unit tests for session management

- **`test_create_session`**: Test the creation of a user session.
- **`test_delete_session`**: Test the deletion of a user session.
- **`test_manage_sessions_valid_session`**: Test the management of a valid user session.
- **`test_manage_sessions_invalid_session`**: Test the management of an invalid user session.
- **`test_get_session_valid_session`**: Test the retrieval of a valid user session.
- **`test_get_session_invalid_session`**: Test the retrieval of an invalid user session.

To run the tests:
    Ensure the web application and MongoDB are set up and running.
    Execute the test using the test runner('test_server.py')

Expected:
    The test should pass without errors.


## User Registration and Authentication

The `user_info.py` script contains functions to register new users and authenticate existing ones against credentials stored in a MongoDB database.
However, this is a stab file. It is made to implement separate user authentication module that is now already implemented in the `do_login` and `profile` method,
in the `server.py` file. The modularisation is a scope for our sprint 3. For now as it is implemented we explain what are the functions that will be implemented.

### Overview

This script provides two primary functions:

- `register_user`: Registers a new user in the database.
- `authenticate_user`: Authenticates a user's login attempt.

### Usage

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

## `search_reviews` Function Documentation

### Overview
The `search_reviews` function is responsible for searching reviews based on a user's query and rendering the search results using the `search_results.tpl` template.
The `search_reviews` function is implemented in the `server.py` file.

### Route Information
- **Route**: `/search_reviews`
- **Method**: GET

### Parameters
- None

### Returns
- **Type**: str
- **Description**: Rendered template with search results (`search_results.tpl` file).

### Functionality
1. Retrieves the search query from the URL's 'query' parameter.
2. Searches for reviews in the 'reviews_collection' with titles or usernames that match the query.
3. Converts ObjectId to string for easier use in the template.
4. Renders the search results using the 'search_results.tpl' template.

### Example Usage
```python
# Example URL: /search_reviews?query=example
search_results = search_reviews()
```

## Other files to take into consideration

### docs folder:

- `attribution_template.md`: A template for attributing work and contributions to the project by team members or third parties.
- `code_review.md`: Outlines our code review process, standards, and checklists to ensure quality and consistency in our codebase.
- `meetingNotes.md`: Notes from our team meetings, capturing the key points discussed, decisions made, and action items.
- `team_review_sprint2.md`: Documentation of peer reviews within the team, reflecting on the work done and providing feedback for improvement.
- `process_model.md`: Outlines the team's sprint process, including a visual model, process components, changes made, and a proposed improvement for continuous documentation updates post-code review and testing.
- `Comp_Arch.md`: Provides an overview of the component architecture of the application, detailing its key components, interactions, and justifications for the chosen architecture.

### doc/images folder: 

- `Process-Model-Diagram.png`: Represents the workflow and stages of a project's development process; how tasks and activities progress from initiation to completion.
- `UML_diagram.png`: Illustrates and communicates the structure, behavior, and interactions of the system or the process of the application.