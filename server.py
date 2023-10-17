from bottle import run, route, template, static_file


@route('/')
def home():
    return template('homepage')


@route('/login')
def login():
    return template('login')

@route('/profile')
def profile():
    return template('profile')

@route('/signup')
def signup():
    return template('signup')

@route('/reviews')
def reviews():
    return template('reviews')





run(debug=True, reloader=True)
