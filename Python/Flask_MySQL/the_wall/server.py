from flask import Flask, request, render_template, redirect, flash, session
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
# will be used to check valid email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "backwards0987654321" #security key
mysql = MySQLConnector(app,'the_wall')
@app.route('/')
def index():
    # render home page with login and registration
    return render_template('login.html')
# routed here if user clicks register on home page

@app.route('/register', methods=['POST'])
def register():
    # validation checks for each entry we ask for
    if str.isalpha(str(request.form['first_name'])) == False:
        flash("First name cannot be empty or contain numbers!")
    if str.isalpha(str(request.form['last_name'])) == False:
        flash("Last name cannot be empty or contain numbers!")
    if len(request.form['password']) < 8:
        flash("Password must be at least 7 characters long!")
    elif request.form['password2'] != request.form['password']:
        flash("Passwords entered do not match!")

    # query to check if email already exists
    email_exists = mysql.query_db("SELECT email_address FROM users WHERE email_address = :email", { 'email': request.form['email'] })
    # check if email entered is in db, if not is it valid
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
        user = mysql.query_db("SELECT * FROM users WHERE email_address = :email;", {'email': request.form['email']})
        print user
        session['id'] = user[0]['id']
        return redirect('/wall')

# routed here if user clicks login on home page
@app.route('/login', methods=['POST'])
def login():
    if len(request.form['password']) < 1 or len(request.form['email']) < 1:
        flash('Incorrect email or password!')
        return redirect('/')
    # create query to return email from database
    query = "SELECT id, first_name, email_address, password FROM users WHERE email_address = :email"
    # grab the users email entered from login
    user = {
    'email': request.form['email'],
    }
    # run query to check email entered
    email = mysql.query_db(query, user)
    if email:
        if bcrypt.check_password_hash(email[0]['password'], request.form['password']):
            # login user
            session['id'] = email[0]['id']
            return redirect('/wall')
        else:
            flash('Incorrect email or password!')
            return redirect('/')
    else:
        # set flash error message and redirect to login page
        flash('Incorrect email or password!')
        return redirect('/')

@app.route('/add_message', methods=['POST'])
def add_message():
    if len(request.form['message']) < 25:
        flash('Messages must be longer than 25 character.')

    if '_flashes' in session:
        return redirect('/wall')

    # make query to add message to db
    query = "INSERT INTO messages (message, users_id, created_at, updated_at) VALUES (:message, :users_id, NOW(), NOW())"

    message = {
        "message" : request.form['message'],
        "users_id" : request.form['user_id'],
    }

    # run query
    mysql.query_db(query, message)
    return redirect('/wall')

@app.route('/add_comment', methods=['POST'])
def add_comment():
    if len(request.form['comment']) > 255:
        flash('Comments cannot exceed 255 characters.')

    if '_flashes' in session:
        return redirect('/wall')
    print "Testing 1"
    print request.form['comment']

    # make query to add message to db
    query = "INSERT INTO comments (comment, messages_id, users_id, created_at, updated_at) VALUES (:comment, :messages_id, :users_id, NOW(), NOW());"
    print "Testing 2"
    comment = {
        "comment" : request.form['comment'],
        "messages_id" : request.form['message_id'],
        "users_id" : request.form['user_id'],
    }
    print comment
    # run query
    print "Testing 3"
    print mysql.query_db(query, comment)
    print "Testing 4"
    return redirect('/wall')

@app.route('/delete_comment/<comment_id>', methods=['POST'])
def delete_comment(comment_id):
    query = "DELETE FROM comments WHERE id = :specific_id;"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {
    'specific_id': comment_id,
    }
    # Run query with inserted data.
    mysql.query_db(query, data)
    return redirect('/wall')

@app.route('/wall')
def wall():
    user= mysql.query_db("SELECT * FROM users WHERE id = :id", {'id': session['id']})

    messages = mysql.query_db("SELECT messages.id, message, messages.created_at, concat(first_name, ' ', last_name) as user FROM messages JOIN users ON messages.users_id = users.id ORDER BY created_at DESC;")

    # query for full joined table of messages, comments and their user association
    messages_comments = mysql.query_db("SELECT concat(users.first_name, ' ', users.last_name) as user, messages.message, messages.id, messages.created_at as 'posted_on', comments.comment, comments.id as 'comment_id', concat(users2.first_name, ' ', users2.last_name) as 'commentor', comments.users_id, comments.created_at as 'commented_on' from users JOIN messages ON users.id = messages.users_id JOIN comments ON messages.id = comments.messages_id JOIN users as users2 on users2.id = comments.users_id ORDER BY comments.created_at ASC;")

    return render_template('wall.html', full_table = messages_comments, message = messages, user = user[0])
app.run(debug=True)
