from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "password"

@app.route('/')
def index():
    session['answer'] = random.randint(1,100)
    print session['answer']
    submit = ''
    button = 'no_win'
    return render_template('index.html', button=button, submit=submit)

@app.route('/guess', methods=['POST'])
def check_guess():
    answer = session['answer']
    guess = request.form['guess']
    results = ''
    if int(guess) == answer:
        print str(session['answer']), "was the number!", request.form['guess']
        results = str(session['answer']) + " was the number!"
        css_style = "correct"
        button2 = "no_win"
        button = "win"
    elif int(guess) > int(session['answer']):
        print "Too high!!!", request.form['guess']
        results = "Too high!!!"
        css_style ="wrong"
        button2 = "blank"
        button = "no_win"
    elif int(guess) < session['answer']:
        print "Too low!!!", request.form['guess']
        results = "Too low!!!"
        css_style = "wrong"
        button2 = "blank"
        button = "no_win"
    return render_template('index.html', results=results, css_style=css_style, button=button, submit=submit)
app.run(debug=True)
