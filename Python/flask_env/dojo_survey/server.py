from flask import Flask, redirect, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = "backwards0987654321" #security key

@app.route('/')
def index():
    #Show home page with entry form
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def info():
    #a check across all inputs to validate if they are acceptable, if not the approriate message will display
    name = request.form['user_name']
    if len(name) < 1:
        flash("Name cannot be empty!")
    comment = request.form['comment']
    if len(comment) < 1:
        flash("Comment cannot be empty!")
    if len(comment) > 120:
        flash("Comment cannot be longer than 120 characters!")
    print len(comment)
    location = request.form['location']
    if len(location) < 1:
        flash("Must select location!")
    language = request.form['language']
    if len(language) < 1:
        flash("Must select language!")

    #if any of the following conditions is met the user will be redirected to entry form page to enter correct information
    if len(name) < 1 or (len(comment) < 1 or len(comment) > 120) or len(location) < 1 or len(language) < 1:
        return redirect('/')

    #if form data is valid, then the results page will summarize info
    return render_template('results.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)
