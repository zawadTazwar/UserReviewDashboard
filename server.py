from bottle import Bottle, run, request, template, static_file

# Create a Bottle web application
app = Bottle()


# Serve static files (CSS)
@app.route('/')
def home():
    return template('homepage')


@app.route('/login')
def login():
    return template('login.tpl')


# Route for handling login form submissions
@app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    # Check if the username and password are correct (in this example, we use a dictionary for user data)
    users = {
        'user1': 'password1',
        'user2': 'password2'
    }

    if username in users and users[username] == password:
        return f"Welcome, {username}! You are now logged in."
    else:
        return "Invalid username or password. Please try again."


@app.route('/profile')
def profile():
    return template('profile')


# Define a route for the sign-up page
@app.route('/signup')
def signup():
    return template('signup.tpl')


# Define a route to handle form submissions
@app.route('/signup', method='POST')
def do_signup():
    username = request.forms.get('username')
    email = request.forms.get('email')
    password = request.forms.get('password')
    confirm_password = request.forms.get('confirm_password')

    # Perform sign-up logic here (e.g., validate input, add to database)
    if not (username and email and password and confirm_password):
        return "All fields are required. Please fill out the form completely."

    if password != confirm_password:
        return "Password and Confirm Password do not match. Please try again."
    # For this example, we'll just return a simple response
    return f"Sign-up successful for {username} with email {email}"


@app.route('/reviews')
def reviews():
    return template('reviews')


if __name__ == '__main__':
    run(app, host='localhost', port=8080)
