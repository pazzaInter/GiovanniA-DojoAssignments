from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
# will be used to check valid email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "backwards0987654321" #security key
mysql = MySQLConnector(app,'users')
@app.route('/')
def index():
    # render home page with login and registration
    return render_template('index.html')

# routed here if user clicks register on home page
@app.route('/register', methods=['POST'])
def register():
    # validation checks for each entry we ask for
    if str.isalpha(str(request.form['first_name'])) == False:
        flash("First name cannot be empty or contain numbers!")
    if str.isalpha(str(request.form['last_name'])) == False:
        flash("Last name cannot be empty or contain numbers!")
    if len(request.form['password']) < 9:
        flash("Password must be longer than 8 characters!")
    elif request.form['password2'] != request.form['password']:
        flash("Passwords entered do not match!")

    # query to check if email already exists
    email_exists = mysql.query_db("SELECT email_address FROM users WHERE email_address = :email", { 'email': request.form['email'] })
    # check if email entered is in db, if not is it valid
    print email_exists
    if email_exists:
        flash("Please enter another email address!")
    elif len(request.form['email']) < 1 or not EMAIL_REGEX.match(str(request.form['email'])):
        flash("Please enter a valid email!")

    # if any flashes from above are created then we jump back to main page
    if '_flashes' in session:
        return redirect('/')
    #if all information entered is valid, then we add the new user
    else:
        # if proper information was entered we will create our query
        query = "INSERT INTO users (first_name, last_name, email_address, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"

        # create a new user which will be added to database
        user = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password']),
        }

        # run query on database with user info to insert
        mysql.query_db(query, user)
        return render_template('success.html', user = request.form['first_name'])

# routed here if user clicks login on home page
@app.route('/login', methods=['POST'])
def login():
    if len(request.form['password']) < 1 or len(request.form['email']) < 1:
        flash('Incorrect email or password!')
        return redirect('/')
    # create query to return email from database
    query = "SELECT first_name, email_address, password FROM users WHERE email_address = :email"
    # grab the users email entered from login
    user = {
    'email': request.form['email'],
    }
    # run query to check email entered
    email = mysql.query_db(query, user)
    print email
    if email:
        print request.form['password']
        if bcrypt.check_password_hash(email[0]['password'], request.form['password']):
            # login user
            return render_template('success.html', user = email[0]['first_name'], login = True )
        else:
            flash('Incorrect email or password!')
            return redirect('/')
    else:
        # set flash error message and redirect to login page
        flash('Incorrect email or password!')
        return redirect('/')
app.run(debug=True)
