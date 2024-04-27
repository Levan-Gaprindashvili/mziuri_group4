from flask import Flask
app=Flask(__name__)

@app.route('/')
def home():
    return "This is main page"

@app.route('/about')
@app.route('/aboutus')
def about():
    return "<h1>This is about us page</h1>"

@app.route('/rugby page')
def rugby_page():
    return "<h2>This is about Rugby page</h2>"