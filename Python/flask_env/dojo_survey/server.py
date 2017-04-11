from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def info():
    name = request.form['user_name']
    print name
    location = request.form['location']
    print location
    language = request.form['language']
    print language
    comment = request.form['comment']
    print comment
    return render_template('results.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)
