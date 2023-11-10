# Component Architecture Document

## Overview
This document provides an architecture overview of a web application built using the Bottle framework in Python. The application's primary focus is on user authentication, session management, and various user interactions, including login, signup, review creation, editing, deletion, and comment addition.

## UML Diagram:
![UML diagram](images/UML_diagram.png)

## Components

### 1. Web Application (Server)

- **Responsibility**: This component serves as the core of the application, handling HTTP requests and responses, routing to the appropriate views, and managing user sessions.
- **Key Functions**:
  - `home()`: Renders the homepage template.
  - `login()`: Renders the login template.
  - `do_login()`: Handles user login and redirects to the dashboard upon success.
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

- **Responsibility**: Manages user sessions and session-related functions.
- 
- **Key Functions**:
  - `create_session(user_id, username, password, first_name, last_name, email, sessions_collection)`: Creates a new user session and sets a session cookie in the response.
  - `delete_session(session_id, sessions_collection)`: Deletes a user session.
  - `manage_sessions(sessions_collection)`: Manages user sessions and acts as a hook to perform session-related tasks.

### 5. Unit Tests

- **Responsibility**: Ensuring the functionality and behavior of various components within the web application through automated testing.
- **Key Test Cases**:
  - `test_home_page()`: Tests the homepage route.
  - `test_login_page()`: Tests the login page route.
  - `test_login()`: Tests user login functionality.
  - `test_profile_page()`: Tests the user profile page route.
  - `test_signup_page()`: Tests the signup page route.
  - `test_create_review_page()`: Tests the create review page route.
  - `test_reviews_page()`: Tests the reviews page route.
  - `test_like_review()`: Tests the "like" functionality for reviews.
  - `test_logout()`: Tests user logout functionality.
  - `test_edit_review_page()`: Tests the edit review page route.
  - `test_update_review()`: Tests updating a review.
  - `test_manage_sessions_valid_session()`: Tests managing a valid user session.
  - `test_manage_sessions_invalid_session()`: Tests managing an invalid user session.
  - `test_get_session_valid_session()`: Tests getting a valid user session.
  - `test_get_session_invalid_session()`: Tests getting an invalid user session.

## Component Interactions

1. **Web Application (Server) to MongoDB Database:**
   - The web application communicates with the MongoDB database to perform data operations, including storing and retrieving user information, reviews, session details, and comments. This interaction ensures that the web application has access to the necessary data for rendering and processing user requests.

2. **Web Application (Server) to Templates:**
   - Views and functions within the web application interact with HTML templates to render user interfaces dynamically. The server component passes data to templates for presentation, enabling the generation of various pages such as the homepage, login page, user profile, and more.

3. **Web Application (Server) to Session Management:**
   - The web application interacts with the session management component to handle user authentication and session-related tasks. Functions like creating a new session, deleting a session, and managing sessions throughout the application are crucial for maintaining user sessions securely.

4. **Web Application (Server) to Unit Tests:**
   - The unit tests component interacts with various parts of the web application to ensure the functionality and behavior of different features. This interaction aids in identifying and addressing issues during development, contributing to the reliability of the overall system.

5. **User Interactions Triggering Server Functions:**
   - User interactions, such as logging in, signing up, creating, editing, or deleting reviews, and adding comments to reviews, trigger corresponding functions within the web application. This interaction ensures that user actions are processed, and the system responds accordingly.

6. **MongoDB Database to Templates:**
   - Templates interact with the MongoDB database to dynamically retrieve and display data, such as review details and comments. This interaction ensures that the presented content is up-to-date and reflects the current state of the data stored in the database.

7. **Session Management to MongoDB Database:**
   - Session management functions interact with the MongoDB database to store and retrieve session-related information. This interaction is crucial for maintaining user sessions securely and tracking user authentication details.

8. **Session Management to Server Functions:**
   - Session management functions act as hooks, interacting with various server functions to perform session-related tasks throughout the application. This interaction ensures consistent and secure session management across different features.


## Quality Attributes:

#### Usability:
The web application is designed with a user-centric approach, aiming to provide an intuitive and seamless experience. Key aspects contributing to usability include:

- **Intuitive Navigation:** The homepage and navigation are designed to be user-friendly, ensuring that users can easily find and access the desired features.

- **Clear Templating:** HTML templates are structured and styled to enhance readability, ensuring that users can quickly understand and interact with the content.

#### Availability:
Key considerations for availability include:

- **Server Reliability:** The web application is hosted on a reliable server infrastructure, minimizing downtime and ensuring users can access the services consistently.

#### Maintainability:
Key factors contributing to maintainability include:

- **Modular Codebase:** The codebase is yet to be structured in a modular fashion, to make it easier to update and maintain individual components without affecting the entire application. That is an objective we have for our next sprint and included in our backlog.

- **Documentation:** Comprehensive documentation accompanies the codebase, providing insights into the architecture, data models, and key functionalities, facilitating smooth maintenance.

#### Testability:
Ensuring the application is testable is crucial for identifying and addressing issues efficiently. Key considerations for testability include:

- **Unit Testing:** The presence of a robust unit testing suite ensures that individual components and functions can be tested in isolation, supporting the identification of bugs and regressions.

## Justifications for the Web Application Architecture

The chosen architecture for the web application offers several advantages that align with the project's requirements and objectives. Here are key justifications for using this architecture:

1. **Simplicity and Readability:**
   - The architecture, based on the Bottle framework in Python, is known for its simplicity and readability. This characteristic facilitates ease of understanding for both current and future development teams, contributing to maintainability.

2. **MongoDB for Flexibility and Scalability:**
   - MongoDB serves as the database management system, providing a NoSQL approach that allows flexibility in handling various types of data. The document-oriented nature of MongoDB supports scalability, enabling the system to adapt to changing data requirements and increased user loads.

3. **Ease of Integration:**
   - The use of MongoDB facilitates seamless integration with the web application. The document-based structure allows for easy mapping between Python objects and database entities, streamlining data retrieval and storage processes.

4. **Clear Component Responsibilities:**
   - The architectural components, such as the web application server, MongoDB database, templates, session management, and unit tests, have well-defined responsibilities. This clear separation of concerns enhances maintainability and modularity.

5. **Automated Testing for Reliability:**
   - The inclusion of a comprehensive set of unit tests ensures the reliability of the application. Automated testing facilitates the identification of bugs and regressions early in the development process, contributing to a more stable and robust system.

6. **Flexibility for Future Enhancements:**
   - The use of a modular codebase and the inclusion of documentation provide a foundation for future enhancements. The architecture is designed to accommodate additional features, improvements, and integrations, supporting the evolution of the web application over time.

## Risk Analysis

### 1. **Security Vulnerabilities:**
   - **Risk:** Inadequate security measures may lead to unauthorized access, data breaches, or other security vulnerabilities.
   - **Mitigation:** Implement secure coding practices, use encryption for sensitive data, conduct regular security audits, and stay updated on security best practices.

### 2. **Dependency on External Services:**
   - **Risk:** Reliance on external services, such as MongoDB and third-party APIs, introduces dependencies that may impact system functionality.
   - **Mitigation:** Have contingency plans for service disruptions, monitor external service status, and consider fallback mechanisms.

### 3. **Lack of Modularity:**
   - **Risk:** A monolithic codebase may hinder the ability to update or replace individual components without affecting the entire application.
   - **Mitigation:** Design the codebase with modularity in mind, follow best practices for code organization, and consider microservices architecture for future scalability.

### 4. **User Experience Challenges:**
   - **Risk:** Poorly designed user interfaces may result in a suboptimal user experience.
   - **Mitigation:** Conduct usability testing, gather user feedback, and iterate on the UI/UX design based on user preferences.

### 5. **Data Loss or Corruption:**
   - **Risk:** Unexpected events, such as server failures or code errors, may lead to data loss or corruption.
   - **Mitigation:** Implement regular data backups, transactional database operations, and error handling mechanisms to minimize the impact of data-related issues.


## Conclusion

In summary, this Component Architecture Document outlines the key components, interactions, quality attributes, justifications, and risks associated with the web application. The chosen architecture, based on the Bottle framework and MongoDB, is justified for its simplicity, flexibility, and potential for future enhancements. The risk analysis highlights areas such as security, external dependencies, modularity, user experience, and data integrity, with corresponding mitigation strategies. Moving forward, the architecture provides a solid foundation for development, emphasizing collaboration, adaptability, and continuous improvement.
