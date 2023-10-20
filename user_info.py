from pymongo import MongoClient

# MongoDB setup
cluster = MongoClient("mongodb+srv://mahadmirza545:Mahad1234@cluster0.yqjy6mb.mongodb.net/?retryWrites=true&w=majority")
db = cluster["userreview"]
users_collection = db["login"]

def register_user(first_name, last_name, username, email, password):
    """
    Registers a new user in the MongoDB database.

    Args:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        username (str): The chosen username.
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        str: A success message if registration is successful, or an error message if the username already exists.
    """
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return "Username already exists. Please choose a different username."

    user_count = users_collection.count_documents({})
    user_id = user_count + 1

    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password  # In a real application, hash the password for security
    }

    users_collection.insert_one(user)
    return f"Sign-up successful for {first_name} {last_name} with username {username}"

def authenticate_user(username, password):
    """
    Authenticates a user by checking the provided username and password.

    Args:
        username (str): The username provided during login.
        password (str): The password provided during login.

    Returns:
        bool: True if the username and password are correct, False otherwise.
    """
    user = users_collection.find_one({"username": username})
    if user and user["password"] == password:
        return True
    return False
