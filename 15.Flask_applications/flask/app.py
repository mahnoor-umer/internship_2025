from flask import Flask, render_template, request

## WSGI
## __name__ : entry point
app = Flask(__name__)

@app.route('/') # rule
def welcome():
    return "Welcome to Microinformatics"

@app.route('/about') 
def about():
    return "<html><h1>Biotech and Data Science Education start-up</h1><html>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

## HTTP verbs,  # GET, POST

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Salam, {name}!"
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)