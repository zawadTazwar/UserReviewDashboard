# User Review System - GitHub Repository README

## Introduction

This GitHub repository contains the code for a User Review System, implemented in Python using the Bottle web framework and PyMongo for MongoDB integration. The system allows users to create accounts, log in, submit reviews, and view their reviews on a dashboard. This README provides an overview of the code and its functionality.

## Code Overview

### Server.py

`server.py` is the main script for the User Review System. It establishes a connection to a MongoDB cluster using the PyMongo library and creates a Bottle web application. The key components of the code are explained below:

- **User Authentication**: Users can register for an account or log in using a username and password. Passwords are stored as-is in this example, but it is recommended to hash them in a real application for security which will hopefully be done in the next sprint.

- **User Dashboard**: Once logged in, users can access their dashboard to view their submitted reviews.

- **Review Submission**: Users can submit reviews that include a title and content.

### Code Authors

- Authors: 
- Jason Wheeler
- Muhammad Mahad Mirza
- Md Jawad Ul Tazwar
- Md Golam Mamud Chowdhury

## Features

1. **User Registration (Sign-Up)**
   - Route URL: `/signup`
   - Parameters:
     - `first_name` (str): The user's first name.
     - `last_name` (str): The user's last name.
     - `username` (str): The desired username for the new account.
     - `email` (str): The user's email address.
     - `password` (str): The password for the new account.
   - Returns:
     - If the `username` is unique, it creates a new user, inserts it into the 'users_collection', and returns a success message.
     - If the `username` is already taken, it returns an error message indicating that the username is not available.

2. **User Login**
   - Route URL: `/login`
   - Parameters:
     - `username` (str): The username provided by the user.
     - `password` (str): The password provided by the user.
   - Returns:
     - If a valid user is found and the password matches, it sets a cookie and redirects to the dashboard.
     - If the user is not found or the password is incorrect, it returns "Invalid username or password."

3. **User Dashboard**
   - Route URL: `/dashboard`
   - Users can view their submitted reviews on the dashboard. If not logged in, they are redirected to the login page. However, for this sprint viewing reviews has not been implemented as it requires session management which we have in mind for the next sprint.

4. **Review Submission**
   - Route URL: `/create_review`
   - Users can create and submit reviews with a title and content. Reviews are stored in the database.

### Usage

To run the application, execute `server.py`. Make sure you have installed the required dependencies, including Bottle and PyMongo.

python server.py

### Future Development
- Session management is mentioned as a requirement for viewing reviews on the dashboard and will be added in the next sprint. This will enhance user authentication and provide a more secure user experience.
    