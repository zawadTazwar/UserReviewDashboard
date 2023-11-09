from bottle import Bottle, request, redirect, template, run, response
from pymongo import MongoClient
from bson import ObjectId
from session_management import create_session, manage_sessions, delete_session, get_session

cluster = MongoClient("mongodb+srv://mahadmirza545:Mahad1234@cluster0.yqjy6mb.mongodb.net/?retryWrites=true&w=majority")
db = cluster["userreview"]
users_collection = db["login"]
sessions_collection = db["sessions"]
print(sessions_collection)
reviews_collection = db["reviews"]
comments_collection = db["comments"]
# Create a Bottle web application
app = Bottle()


@app.route('/')
def home():
    """
    Author: Jason Wheeler
    Main page when opening the website.

    Returns:
        the homepage.tpl file.
    """
    return template('homepage')


@app.route('/login')
def login():
    """
    Author: Jason Wheeler
    Login page /login

    Returns:
        the login.tpl file.
    """
    return template('login.tpl')


@app.hook('before_request')
def session_manager():
    manage_sessions(sessions_collection)


@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    user = users_collection.find_one({"username": username})

    user_id = user["id"]
    first_name = user["first_name"]
    last_name = user["last_name"]
    email = user["email"]

    if user and user["password"] == password:
        session_id = create_session(user_id, username, password, first_name, last_name, email, sessions_collection)
        response.set_cookie('session_id', session_id)
        redirect('/dashboard')
    else:
        return "Invalid username or password"


@app.route('/profile')
def profile():
    # Retrieve user information from the session if session exists
    session = get_session(request)
    if not session:
        return redirect('/login')
    username = request.session.get('username', None)
    first_name = request.session.get('first_name', None)
    last_name = request.session.get('last_name', None)
    email = request.session.get('email', None)

    # Pass the user data to the profile template
    return template('profile', username=username, first_name=first_name, last_name=last_name, email=email)


# Define a route for the sign-up page
@app.route('/signup')
def signup():
    """
    Author: Jason Wheeler
    Signup page /signup

    Returns:
        the signup.tpl file.
    """
    return template('signup.tpl')


@app.route('/signup', method='POST')
def do_signup():
    first_name = request.forms.get('first_name')
    last_name = request.forms.get('last_name')
    username = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('password')

    # Check if the username already exists
    existing_user = users_collection.find_one({"username": username})
    if existing_user:
        return "Username already exists. Please choose a different username."

    # Count the number of existing users to generate a unique ID
    user_count = users_collection.count_documents({})
    user_id = user_count + 1

    # Create a new user document
    user = {
        "id": user_id,
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password  # Note: In a real application, hash the password for security
    }

    # Insert the new user into the 'users_collection'
    users_collection.insert_one(user)

    # For this example, you can return a success message
    return f"Sign-up successful for {first_name} {last_name} with username {username}"


@app.route('/reviews')
def reviews():
    # Fetch review titles and their corresponding _id from the database
    reviews = list(reviews_collection.find({}, {"_id": 1, "title": 1}))

    # Modify the _id field to a string
    for review in reviews:
        review['_id'] = str(review['_id'])

    return template('reviews.tpl', reviews=reviews)


@app.route('/view_review/<review_id>')
def view_review(review_id):
    review = reviews_collection.find_one({"_id": ObjectId(review_id)})
    comments = comments_collection.find({"review_id": review_id})
    if not review:
        return "Review not found"

    return template('view_review.tpl', review=review, comments=comments)


@app.route('/dashboard')
def dashboard():
    username = request.session.get('username', None)

    # Fetch user reviews from the database
    user_reviews = list(reviews_collection.find({'username': username}, {"_id": 1, "title": 1, "content": 1}))

    # Modify the _id field to a string
    for review in user_reviews:
        review['_id'] = str(review['_id'])

    return template('dashboard.tpl', reviews=user_reviews)


# Route for editing a review
@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    review = reviews_collection.find_one({"_id": ObjectId(review_id)})

    if not review:
        return "Review not found"

    return template('edit_review.tpl', review=review)


# Route for updating a review after editing
@app.route('/update_review', method='POST')
def update_review():
    review_id = request.forms.get('review_id')
    content = request.forms.get('content')

    reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$set": {"content": content}})

    redirect('/dashboard')


@app.route('/delete_review/<review_id>', method='POST')
def delete_review(review_id):
    reviews_collection.delete_one({"_id": ObjectId(review_id)})
    return redirect('/dashboard')


# Route for creating a new review
@app.route('/create_review')
def create_review():
    return template('create_review.tpl')


@app.route('/store_review', method='POST')
def store_review():
    title = request.forms.get('title')
    content = request.forms.get('content')
    username = request.session.get('username')

    review = {
        "username": username,
        "title": title,
        "content": content,
        "like": 0,
        "dislike": 0
    }

    reviews_collection.insert_one(review)

    redirect('/dashboard')


@app.route('/like_review/<review_id>', method='POST')
def like_review(review_id):
    action = request.forms.get('action')

    if action == 'like':
        reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$inc": {"like": 1}})
    elif action == 'dislike':
        reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$inc": {"dislike": 1}})

    # Redirect back to the view_review page
    redirect(f'/view_review/{review_id}')


@app.route('/logout')
def logout():
    # Clear the session
    session_id = request.get_cookie('session_id')
    if session_id:
        delete_session(session_id, sessions_collection)
        response.delete_cookie('session_id')
    redirect('/login')


@app.route('/add_comment/<review_id>', method=['GET', 'POST'])
def comment(review_id):
    if request.method == 'POST':
        content = request.forms.get('comment')

        if content:
            username = request.session.get('username')
            comment = {
                "review_id": review_id,
                "username": username,
                "comment": content,
            }

            comments_collection.insert_one(comment)
            redirect('/view_review/' + review_id)
    else:
        # Handle GET request to display comments
        review = reviews_collection.find_one({"_id": ObjectId(review_id)})
        comments = comments_collection.find({"review_id": review_id})
        return template('view_review.tpl', review=review, comments=comments)


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
