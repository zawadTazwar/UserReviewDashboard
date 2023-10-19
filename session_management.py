import secrets

# In-memory session storage
sessions = {}

def create_session(request, response):
    session_id = secrets.token_hex(16)
    sessions[session_id] = {}
    response.set_cookie('session_id', session_id)

def get_session(request):
    session_id = request.get_cookie('session_id')
    if session_id in sessions:
        return sessions[session_id]
    return {}
