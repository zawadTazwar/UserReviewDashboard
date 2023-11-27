from bottle import Bottle, request, redirect, template, run, response
from pymongo import MongoClient
from bson import ObjectId
from session_management import create_session, manage_sessions, delete_session, get_session
import sendgrid
from sendgrid.helpers.mail import Mail



# Initialize a connection to a MongoDB cluster and set up database and collections.
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


@app.route('/contactus')
def contact():
    return template('contact_us.tpl')


@app.hook('before_request')
def session_manager():
    """
    Hook function for managing user sessions before processing each request.

    This function utilizes the `manage_sessions` function to handle tasks related to user sessions
    before the application processes each incoming request.

    Args:
        None

    Returns:
        None
    """
    manage_sessions(sessions_collection)


@app.route('/login', method='POST')
def do_login():
    """
    Handle user login when a POST request is received.

    Retrieves the username and password from the request form, attempts to authenticate the user.
    If authentication is successful, a new session is created, and the user is redirected to the dashboard.
    If the login is unsuccessful, an "Invalid username or password" message is returned.

    Returns:
        HTTP response: Redirects to the dashboard upon successful login or provides an error message.
    """
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


@app.route('/forgot_password')
def forgot_password():
    return template('forgot_password.tpl')


@app.route('/profile')
@app.route('/profile/<username>')
def profile(username=None):
    """
    Display the user's profile based on the provided username or session.

    Args:
        username (str): The username of the profile to be viewed.

    Returns:
        HTTP response: The user's profile page or a redirect to the login page.
    """

    # Check if there's an active session
    session = get_session(request)

    # If no username provided, try fetching from session
    if not username:
        if not session:
            return redirect('/login')
        username = session.get('username')

    # Retrieve user information from the database using the provided or session username
    user = users_collection.find_one({"username": username})

    # If the user doesn't exist, display a message
    if not user:
        return "User not found"

    # Fetch user reviews based on the retrieved username
    user_reviews = list(reviews_collection.find({'username': username}, {"_id": 1, "title": 1}))
    for review in user_reviews:
        review['_id'] = str(review['_id'])

    # Pass the user data to the profile template
    return template('profile.tpl', username=user.get('username'), first_name=user.get('first_name'),
                    last_name=user.get('last_name'), email=user.get('email'), reviews=user_reviews)

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
    """
    Author: Mahad
    Handle user registration (sign-up) when a POST request is received.

    Parses user registration data from the request form, checks for duplicate usernames,
    generates a unique user ID, and inserts the new user into the 'users_collection'.

    Returns:
        str: A success message indicating the user's sign-up status.
    """
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


@app.route('/top_reviewers')
def top_reviewers():
    return template('top_reviewer.tpl')


@app.route('/reviews')
def reviews():
    """
    Fetches review titles and corresponding _id from the database.

    Returns:
        template: 'reviews.tpl' with reviews data.
    """

    # Fetch review titles and their corresponding _id from the database
    reviews = list(reviews_collection.find({}, {"_id": 1, "title": 1}))

    # Modify the _id field to a string
    for review in reviews:
        review['_id'] = str(review['_id'])

    return template('reviews.tpl', reviews=reviews)


@app.route('/view_review/<review_id>')
def view_review(review_id):
    """
    Retrieves and displays a specific review and its comments.

    Args:
        review_id (str): The unique identifier for the review.

    Returns:
        template: 'view_review.tpl' with review and comments data.
        str: "Review not found" if the review does not exist.
    """

    review = reviews_collection.find_one({"_id": ObjectId(review_id)})
    comments = comments_collection.find({"review_id": review_id})

    if not review:
        return "Review not found"

    return template('view_review.tpl', review=review, comments=comments)


@app.route('/dashboard')
def dashboard():
    """
    Displays the dashboard with reviews created by the logged-in user.

    Returns:
        template: 'dashboard.tpl' with user reviews data.
    """

    username = request.session.get('username', None)

    # Fetch user reviews from the database
    user_reviews = list(reviews_collection.find({'username': username}, {"_id": 1, "title": 1, "content": 1}))

    # Modify the _id field to a string
    for review in user_reviews:
        review['_id'] = str(review['_id'])

    return template('dashboard.tpl', reviews=user_reviews)


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    """
    Displays the page for editing a specific review.

    Args:
        review_id (str): The unique identifier for the review.

    Returns:
        template: 'edit_review.tpl' with review data.
        str: "Review not found" if the review does not exist.
    """

    review = reviews_collection.find_one({"_id": ObjectId(review_id)})

    if not review:
        return "Review not found"

    return template('edit_review.tpl', review=review)


@app.route('/update_review', method='POST')
def update_review():
    """
    Updates a review based on the provided content.

    Form Data:
        review_id (str): The unique identifier for the review.
        content (str): The updated content for the review.

    Redirects:
        '/dashboard' after updating the review.
    """

    review_id = request.forms.get('review_id')
    content = request.forms.get('content')

    reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$set": {"content": content}})

    redirect('/dashboard')


@app.route('/delete_review/<review_id>', method='POST')
def delete_review(review_id):
    """
    Deletes a specific review.

    Args:
        review_id (str): The unique identifier for the review.

    Redirects:
        '/dashboard' after deleting the review.
    """

    reviews_collection.delete_one({"_id": ObjectId(review_id)})
    return redirect('/dashboard')


@app.route('/create_review')
def create_review():
    """
    Displays the page for creating a new review.

    Returns:
        template: 'create_review.tpl'.
    """

    return template('create_review.tpl')


@app.route('/store_review', method='POST')
def store_review():
    """
    Stores a new review in the database.

    Form Data:
        title (str): The title of the review.
        content (str): The content of the review.

    Redirects:
        '/dashboard' after storing the review.
    """

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
    """
    Handles the 'like' or 'dislike' action for a review.

    Form Data:
        action (str): The action to perform ('like' or 'dislike').

    Redirects:
        '/view_review/{review_id}' after processing the action.
    """

    action = request.forms.get('action')

    if action == 'like':
        reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$inc": {"like": 1}})
    elif action == 'dislike':
        reviews_collection.update_one({"_id": ObjectId(review_id)}, {"$inc": {"dislike": 1}})

    # Redirect back to the view_review page
    redirect(f'/view_review/{review_id}')


@app.route('/logout')
def logout():
    """
    Endpoint for logging out a user.

    This route clears the user session by deleting the associated session data from the database
    and removing the session ID cookie from the user's browser.

    Args:
        None

    Returns:
        None
    """
    # Clear the session
    session_id = request.get_cookie('session_id')
    if session_id:
        delete_session(session_id, sessions_collection)
        response.delete_cookie('session_id')
    redirect('/login')


@app.route('/search_reviews', method='GET')
def search_reviews():
    """
    Author: Md Golam Mahmud Chowdhury
    Search reviews / search_reviews

    Returns:
        the search_results.tpl file.

    Search for reviews that match a user's query.

    This route retrieves a search query from the URL's 'query' parameter and searches for reviews in the 'reviews_collection' with titles or usernames that match the query. It returns the search results using a template.

    Returns:
        str: Rendered template with search results.
    """
    # Get the search query from the URL
    query = request.query.query.strip()  # The 'query' parameter from the URL

    # Search for reviews in the 'reviews_collection' with titles or usernames that match the query
    results = list(reviews_collection.find({
        "$or": [
            {"title": {"$regex": query, "$options": "i"}},
            {"username": {"$regex": query, "$options": "i"}}
        ]
    }))

    # Convert ObjectId to string for easier use in the template
    for review in results:
        review["_id"] = str(review["_id"])

    # Render the search results using a template
    return template('search_results', reviews=results)


@app.route('/add_comment/<review_id>', method=['GET', 'POST'])
def comment(review_id):
    """
    Author: Mahad
    Handle adding comments to a review specified by its unique ID.

    Args:
        review_id (str): The unique identifier of the review to which comments are being added.

    Returns:
        HTTP response: Redirects to the review view after comment addition.
    """
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

    return template('error', error=str(e))


@app.route('/submit_inquiry', method='POST')
def submit_inquiry():
    """
    Handles the submission of inquiry form data and sends an email using SendGrid API.

    Returns:
        HTTP response: Indicates success or failure of the email sending process.
    """

    # Get the SendGrid API key from the environment variables
    api_key = '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'
    sg = sendgrid.SendGridAPIClient(api_key)

    # Replace with your sender and receiver emails
    sender_email = 'mgmchowdhury@mun.ca'
    receiver_email = 'g.mahmud.chowdhury@gmail.com'

    # Extract form data
    username = request.forms.get('username')
    name = request.forms.get('name')
    email = request.forms.get('email')
    subject = request.forms.get('subject')
    content = request.forms.get('content')

    # Compose the email message
    message = Mail(
        from_email=sender_email,
        to_emails=receiver_email,
        subject=subject,
        html_content=f"<strong>From:</strong> {username} ({name})<br><strong>Email:</strong> {email}<br><br>{content}"
    )

    try:
        # Send the email using SendGrid API

        response = sg.send(message)

        # Check if email sending was successful
        if response.status_code == 202:
            return "Email sent successfully!"
        else:
            return "Failed to send email. Please try again later."
    except Exception as e:
        return f"Failed to send email: {str(e)}"


@app.route('/contact_us')
def contact_us():
    """
    Displays the contact us page.

    Returns:
        HTML template: Renders the contact us page template.
    """
    return template('contact_us.tpl')

if __name__ == '__main__':
    run(app, host='localhost', port=8080)
