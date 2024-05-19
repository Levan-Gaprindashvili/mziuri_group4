from flask import Flask, request, render_template,redirect, url_for
app = Flask(__name__)


tasks =["Xhinkali", "Xhachapuri", "Lobiani", "Puri", "Yveli"]


@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)



@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('home'))
    return render_template('add_task.html' , tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)

