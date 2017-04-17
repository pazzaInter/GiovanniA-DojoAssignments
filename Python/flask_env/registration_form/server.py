from flask import Flask, render_template, request, redirect, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "backwards0987654321" #security key

@app.route('/')
def index():
    if 'users' not in session:
        session['users'] = []

    return render_template('index.html')

@app.route('/user', methods=['POST'])
def add_user():
    if str.isalpha(str(request.form['f_name'])) == False:
        flash("First name cannot be empty or contain numbers!")
    if str.isalpha(str(request.form['l_name'])) == False:
        flash("Last name cannot be empty or contain numbers!")
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(str(request.form['email'])):
        flash("Please enter a valid email!")
    if len(request.form['password']) < 9:
        flash("Password must be longer than 8 characters!")
    if request.form['c_password'] != request.form['password']:
        flash("Passwords entered do not match!")

    #if any of the abover conditions were caught, this will prompt user to renter correct information
    if str.isalpha(str(request.form['f_name'])) == False or str.isalpha(str(request.form['l_name'])) == False or len(request.form['email']) < 1 or (len(request.form['password']) < 9) or (request.form['c_password'] != request.form['password']) or not EMAIL_REGEX.match(request.form['email']):
        return redirect('/')

    #if all information entered is valid, then we add the new user
    else:
        #create a new user
        user = {
        'first_name': str(request.form['f_name']),
        'last_name': str(request.form['l_name']),
        'email': str(request.form['email']),
        'password': str(request.form['password'])
        }
        #add our new user to our list of users
        session['users'].append(user)
        flash("Thanks for submitting your information!")
        return redirect('/')

app.run(debug=True)
