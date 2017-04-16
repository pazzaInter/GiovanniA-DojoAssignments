from flask import Flask, render_template, redirect, request, session
import random, time

app = Flask(__name__)

app.secret_key = "backwards0987654321" #security key

@app.route('/')
def index():
    try:
        #will check if gold has already been created, if not then set to 0
        session['gold'] = session['gold']
    except KeyError:
        session['gold'] = 0
    try:
        #will check if log has been created, if not then create an empty list
        session['log'] != session['log']
    except KeyError:
        session['log'] = []
    return render_template('index.html')

@app.route('/process_money', methods=["POST"])
def money_calc():
    #if True then gold was earned, if set to False then gold was lost
    session['gain_loss'] = True
    if request.form['building'] == 'farm':
        earned = random.randint(10,20)
        logdate = time.strftime("%Y/%m/%d %I:%M %p")
        session['gold'] += earned
        session['gain_loss'] = True
        session['log'].append(["Earned {} golds from the {}! ({})".format(earned, request.form['building'], logdate), True])
    elif request.form['building'] == 'cave':
        earned = random.randint(5,10)
        logdate = time.strftime("%Y/%m/%d %I:%M %p")
        session['gold'] += earned
        session['gain_loss'] = True
        session['log'].append(["Earned {} golds from the {}! ({})".format(earned, request.form['building'], logdate), True])
    elif request.form['building'] == 'house':
        earned = random.randint(2,5)
        logdate = time.strftime("%Y/%m/%d %I:%M %p")
        session['gold'] += earned
        session['gain_loss'] = True
        session['log'].append(["Earned {} golds from the {}! ({})".format(earned, request.form['building'], logdate), True])
    elif request.form['building'] == 'casino':
        earn_lose = random.randint(0,1)
        logdate = time.strftime("%Y/%m/%d %I:%M %p")
        if  earn_lose == 1: # this will earn the ninja money
            earned = random.randint(0,50)
            session['gold'] += earned
            session['gain_loss'] = True
            session['log'].append(["Earned {} golds from the {}! ({})".format(earned, request.form['building'], logdate), True])
        elif earn_lose == 0:
            lost = random.randint(0,50)
            session['gold'] -= lost
            session['gain_loss'] = False
            session['log'].append(["Entered a {} and lost {} golds... Ouch.. ({})".format(request.form['building'], lost, logdate), False])
    for each in session['log']:
        print each
        print each[0]
    return redirect('/')

@app.route('/reset', methods=['POST'])
def new_game():
    #this will reset the game to clear all gold collected/lost
    session.clear()
    return redirect('/')

app.run(debug=True)
