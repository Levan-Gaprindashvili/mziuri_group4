from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///books.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(200), nullable=False)


@app.route("/")
def home():
    all_books = Books.query.all()
    return render_template("index.hmtl", name="book", books=all_books)

@app.route("/book/<int:book_id>")
def book(book_id):
    book = Books.querry.get(book_id)
    if not book:
        abort(404)
    return render_template("book.hmtl", name="book")

@app.route("/add_book", methods=["POST", "GET"])
def add_book(author=None, title=None, year=None):
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]

        new_book = Books(title=title, author=author, year=year)

        db.session.add(new_book)
        db.session.commit(new_book)

        return redirect("/")
    else:
        return render_template("add_book.html", name="add_book")