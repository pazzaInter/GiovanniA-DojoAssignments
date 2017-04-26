from flask import Flask, request, redirect, render_template, flash
# import the Connector function
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "backwards0987654321" #security key
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'emails')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/success', methods=['POST'])
def add_email():
    if EMAIL_REGEX.match(str(request.form['email'])):
        query = "INSERT INTO emails (email_address, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = { 'email': request.form['email'] }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        # Run query to retrieve values from db
        emails = mysql.query_db("Select * FROM emails")
        print emails
        return render_template('success.html', emails = emails)
    else:
        flash("Email is not valid")
        return redirect('/')
app.run(debug=True)
