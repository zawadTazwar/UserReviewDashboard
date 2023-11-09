# Component Architecture Document

## Overview

This document provides an architecture overview of a web application built using the Bottle framework in Python. The application's primary focus is on user authentication, session management, and various user interactions, including login, signup, review creation, editing, deletion, and comment addition.

### UML Diagram:
![UML diagram](images/UML diagram.png)

## Components

### 1. Web Application (Server)

- **Responsibility**: This component serves as the core of the application, handling HTTP requests and responses, routing to the appropriate views, and managing user sessions.
- **Key Functions**:
  - `home()`: Renders the homepage template.
  - `login()`: Renders the login template.
  -  `do_login()`: Handles user login and redirects to the dashboard upon success.
  - `profile_info()`: Manages the user's profile information.
  - `profile()`: Renders the user profile page.
  - `signup()`: Renders the signup template.
  - `do_signup()`: Handles user registration.
  - `reviews()`: Lists available reviews.
  - `view_review(review_id)`: Displays a specific review and associated comments.
  - `dashboard()`: Displays the user's dashboard with their reviews.
  - `edit_review(review_id)`: Allows editing a review.
  - `update_review()`: Handles review updates.
  - `delete_review(review_id)`: Handles review deletions.
  - `create_review()`: Renders the create_review template.
  - `store_review()`: Handles the creation of new reviews.
  - `add_comment(review_id)`: Allows users to add comments to reviews.
  - `logout()`: Logs the user out and clears the session.
  

### 2. MongoDB Database

- **Responsibility**: This component stores user data, review data, and session information in a MongoDB database.
- **Key Collections**:
  - `users_collection`: Stores user information, including username, password, first name, last name, and email.
  - `reviews_collection`: Stores review data, including titles, content, likes, and dislikes.
  - `sessions_collection`: Stores session data for user authentication and session management.
  - `comments_collection`: Stores comments associated with reviews.

  
### 3. Templates

- **Responsibility**: This component is responsible for rendering HTML templates to present information to the user and handle user interactions.
- **Key Views and Templates**:
  - 'homepage.tpl': Main page when opening the website.
  - 'login.tpl': Login page.
  - 'profile.tpl': User profile page.
  - 'signup.tpl': Signup page.
  - 'reviews.tpl': Reviews page.
  - 'view_review.tpl': View a single review.
  - 'dashboard.tpl': User dashboard page.
  - 'edit_review.tpl': Edit a review.
  - 'create_review.tpl': Create a new review.
  - 'search_results.tpl': Display search results.
  

### 4. Session Management

- **Responsibility**: This component manages user sessions and session-related functions.
- **Key Functions**:
  - `create_session(user_id, username, password, first_name, last_name, email, sessions_collection)`: Creates a new user session and sets a session cookie in the response.
  - `delete_session(session_id, sessions_collection)`: Deletes a user session.
  - `manage_sessions(sessions_collection)`: Manages user sessions and acts as a hook to perform session-related tasks.

## Component Interactions

The components interact as follows:

1. Users access the web application through their web browsers.

2. The web application (Bottle) receives HTTP requests from users.

3. Upon receiving a request, the web application routes it to the appropriate view or function based on the URL path.

4. Views and templates render HTML pages for user interaction.

5. The application interacts with the MongoDB database to store and retrieve user data, reviews, and session information.

6. Session management functions handle user authentication and session creation, while hooks manage user sessions throughout the application.

7. Views and templates access the MongoDB database to retrieve review data and comments for rendering.

8. Users can perform actions such as logging in, signing up, creating, editing, or deleting reviews, and adding comments to reviews.

9. Session data is stored in the MongoDB collection designated for sessions, and session cookies are set in users' browsers.

10. User data is retrieved from the database for authentication and personalization.

## Conclusion

This component architecture document outlines the various components, their responsibilities, and interactions in the web application. The components work together to provide user authentication, session management, and features for creating and managing reviews and comments. MongoDB is used to store and retrieve data, while the Bottle framework handles routing and view rendering.
