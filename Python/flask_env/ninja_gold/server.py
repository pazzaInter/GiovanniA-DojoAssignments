from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)

app.secret_key = "backwards0987654321" #security key

@app.route('/')
def index():
    try:
        session['gold'] = session['gold']
    except KeyError:
        session['gold'] = 0
    try:
        session['log'] != session['log']
    except KeyError:
        session['log'] = []
    # if session['log'] != session['log']:
    #     session['log'] = []
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def money_calc():
    print request.form['building']
    if request.form['building'] == 'farm':
        session['gold'] += random.randint(10,20)
        session['log'].append("You clicked farm")
    elif request.form['building'] == 'cave':
        session['gold'] += random.randint(5,10)
        session['log'].append("You clicked cave")
    elif request.form['building'] == 'house':
        session['gold'] += random.randint(2,5)
        session['log'].append("You clicked house")
    elif request.form['building'] == 'casino':
        earn_lose = random.randint(0,1)
        print earn_lose
        if  earn_lose == 1: # this will earn the ninja money
            session['gold'] += random.randint(0,50)
            session['log'].append("You clicked casino")
        elif earn_lose == 0:
            session['gold'] -= random.randint(0,50)
            session['log'].append("You clicked casino")
    print session['gold']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def new_game():
    #this will reset the game to clear all gold collected/lost
    session.clear()
    return redirect('/')

app.run(debug=True)
