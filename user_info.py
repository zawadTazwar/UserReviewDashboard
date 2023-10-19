users = {
    'user1': {
        'password': 'password1',
        'email': 'user1@example.com',
    },
    'user2': {
        'password': 'password2',
        'email': 'user2@example.com',
    },
}

def register_user(username, password, email):
    if username in users:
        return False  # User already exists
    users[username] = {'password': password, 'email': email}
    return True

def authenticate_user(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return True
    return False
