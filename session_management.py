from bottle import Bottle, request, response, template
import secrets
from bson import ObjectId

# A dictionary to store user sessions identified by session_id
sessions = {}


def create_session(user_id, username, password, first_name, last_name, email, sessions_collection):

    """
    Create a new user session and set a session cookie in the response.

    This function generates a unique session ID, creates a session document, and stores it in the MongoDB collection
    designated for sessions. It also stores the session data in a dictionary for quick access.

    Args:
        user_id (int): The unique identifier of the authenticated user.
        username (str): The username of the authenticated user.
        password (str): The password of the authenticated user.
        first_name (str): The first name of the authenticated user.
        last_name (str): The last name of the authenticated user.
        email (str): The email address of the authenticated user.
        sessions_collection (pymongo.collection.Collection): The MongoDB collection for storing sessions.

    Returns:
        str: The newly created session ID, which can be used as a session identifier.
    """
    session_id = ObjectId()  # Generate a unique session ID

    session_data = {
        "_id": session_id,
        "id": user_id,
        "username": username,

        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password
        # Add other session data as needed
    }
    sessions_collection.insert_one(session_data)

    # Store the session data in the dictionary for quick access
    sessions[str(session_id)] = session_data

    return str(session_id)


def delete_session(session_id, sessions_collection):
    """
    Deletes the user session associated with the provided session ID.

    Args:
        session_id (str): The session ID of the session to be deleted.
        sessions_collection (pymongo.collection.Collection): The MongoDB collection for storing sessions.

    Returns:
        None
    """
    sessions_collection.delete_one({"_id": ObjectId(session_id)})

    # Remove the session data from the dictionary
    if session_id in sessions:
        del sessions[session_id]


def manage_sessions(sessions_collection):
    """
    Manages user sessions. This function should be used as a hook before processing requests.

    Args:
        sessions_collection (pymongo.collection.Collection): The MongoDB collection for storing sessions.

    Returns:
        None
    """
    session_id = request.get_cookie('session_id')
    if session_id:
        session = sessions.get(session_id)

        if not session:
            # Invalid session, clear the cookie
            response.delete_cookie('session_id')
        else:
            # Session is valid; you can access session data like session['username']
            request.session = session


def get_session(request):
    """
    Retrieves the user session associated with the provided request.

    Args:
        request (bottle.Request): The incoming HTTP request containing the session cookie.

    Returns:
        dict: A dictionary representing the user session data. An empty dictionary is returned if no session is found.
    """
    session_id = request.get_cookie('session_id')
    return sessions.get(session_id, {})




