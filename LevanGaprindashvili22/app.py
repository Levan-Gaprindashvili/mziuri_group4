from flask import Flask, session, render_template, redirect, request, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secret_key"
app.permanent_session_lifetime = timedelta(seconds=10)
users = {'Levani': 'password123'}


@app.route("/")
def index():
    return render_template('base.html', name='base')


@app.route("/home")
def home():
    if not 'user' in session:
        return redirect(url_for('login'))
    return render_template('home.html', name='home')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users.get(username, None) == password:
            session['user'] = username
            return redirect(url_for('home'))
    return render_template('login.html', name='login')

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)