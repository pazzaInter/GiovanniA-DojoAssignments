from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
# will be used to check valid email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "backwards0987654321" #security key
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    # run query to return all rows in db and display friends
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
    # only add a friend to the database if following condtions fail!
    if str.isalpha(str(request.form['first_name'])) == False:
        flash("Please enter a valid first name!")
    if str.isalpha(str(request.form['last_name'])) == False:
        flash("Please enter a valid last name!")
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(str(request.form['email'])):
        flash("Please enter a valid email!")

    #if any of the abover conditions were caught, this will prompt user to renter correct information
    if str.isalpha(str(request.form['first_name'])) == False or str.isalpha(str(request.form['last_name'])) == False or not EMAIL_REGEX.match(request.form['email']):
        return redirect('/')

    else:
        # proper information was entered and we create our query
        query = "INSERT INTO friends (first_name, last_name, email_address, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
         'first_name': request.form['first_name'],
         'last_name':  request.form['last_name'],
         'email': request.form['email']
        }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/')
@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    # Write query to select specific user by id.
    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('update.html', friend=friends[0])
@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "UPDATE friends SET first_name= :first_name, last_name= :last_name, email_address= :email, updated_at=now() WHERE id = :specific_id;"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {
    'specific_id': friend_id,
    'first_name' : request.form['first_name'],
    'last_name' : request.form['last_name'],
    'email' : request.form['email'],
    }
    # Run query with inserted data.
    new_friends = mysql.query_db(query, data)
    return redirect('/')
@app.route('/friends/<friend_id>/delete', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE id = :specific_id;"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {
    'specific_id': friend_id,
    }
    # Run query with inserted data.
    new_friends = mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
