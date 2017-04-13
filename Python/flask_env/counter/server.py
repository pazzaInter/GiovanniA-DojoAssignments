from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "backwards0987654321" #security key
@app.route('/')
def index():
    #each time page is loaded, counter will increase by 1
    session['counter'] += 1
    return render_template('index.html')
@app.route('/increment', methods=['POST'])
def increment():
    #if buttom is pressed on page, counter will jump by 2 - 1 for button press and then also for page reload
    print request.form['plus_1']
    session['counter'] += int(request.form['plus_1'])
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    #if button is pressed then it will reset counter to 0
    session['counter'] = 0
    return redirect('/')
app.run(debug = True)
