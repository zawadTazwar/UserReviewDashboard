import secrets

# A dictionary to store user sessions identified by session_id
sessions = {}

def create_session(request, response):
    """
    Creates a new user session and set a session cookie in the response.

    Args:
        request (bottle.Request): The incoming HTTP request.
        response (bottle.Response): The HTTP response where the session cookie will be set.

    Returns:
        None
    """
    session_id = secrets.token_hex(16)
    sessions[session_id] = {}
    response.set_cookie('session_id', session_id)

def get_session(request):
    """
    Retrieves the user session associated with the provided request.

    Args:
        request (bottle.Request): The incoming HTTP request containing the session cookie.

    Returns:
        dict: A dictionary representing the user session data. An empty dictionary is returned if no session is found.
    """
    session_id = request.get_cookie('session_id')
    if session_id in sessions:
        return sessions[session_id]
    return {}
