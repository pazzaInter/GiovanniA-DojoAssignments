from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "backwards0987654321" #security key

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/ninja/')
def ninjas():
    color = 'none'
    return render_template('ninjas.html', color = color)

@app.route('/ninja/<color>')
def ninjas_color(color):
    print color
    ninja = ''
    if color == 'purple':
        ninja = 'donatello'
    elif color == 'blue':
        ninja = 'leonardo'
    elif color == 'orange':
        ninja = 'michelangelo'
    elif color == 'red':
        ninja = 'raphael'
    else:
        ninja = 'notapril'
    print ninja
    return render_template('ninjas.html', ninja = ninja)

app.run(debug=True)
