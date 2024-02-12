from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
app.app_context().push()

#Create model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=False)
    author = db.Column(db.String(120), unique=False)
    publisher = db.Column(db.String(120), unique=False)

    def __repr__(self):
        return f"{self.book_name} - {self.publisher} - {self.publisher}"

def add_book(book_name,author,publisher):
    book = Book()
    book.book_name=book_name
    book.author=author
    book.publisher=publisher

    db.create_all()
    db.session.add(book)
    db.session.commit()

def edit_book(id,book_name,author,publisher):
    book = Book.query.get(id)
    book.book_name=book_name
    book.author=author
    book.publisher=publisher

    db.create_all()
    db.session.add(book)
    db.session.commit()

def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}

    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!@"}

@app.route('/')
def index():
    return 'Hello!'

#Display all books in DB
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []

    for book in books:
        book_date = {'book_name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_date)
    return {'books': output}

@app.route('/entry-form', methods=['GET', 'POST'])
def entry_form():
    # handle the POST request
    if request.method == 'POST':
        add_book(request.form.get('book_name'), request.form.get('author'), request.form.get('publisher'))

    # otherwise handle the GET request
    return '''
           <form method="POST">
                <div><label>Book Name: <input type="text" name="book_name"></label></div>
                <div><label>Author: <input type="text" name="author"></label></div>
                <div><label>Publisher: <input type="text" name="publisher"></label></div>
                <input type="submit" value="Submit">
           </form>'''

@app.route('/edit-form', methods=['GET', 'POST'])
def edit_form():
    # handle the POST request
    if request.method == 'POST':
        edit_book(request.form.get('id'), request.form.get('book_name'), request.form.get('author'), request.form.get('publisher'))

    # otherwise handle the GET request
    return '''
           <form method="POST">
                <div><label>ID: <input type="integer" name="id"></label></div>
                <div><label>Book Name: <input type="text" name="book_name"></label></div>
                <div><label>Author: <input type="text" name="author"></label></div>
                <div><label>Publisher: <input type="text" name="publisher"></label></div>
                <input type="submit" value="Submit">
           </form>'''

@app.route('/delete-form', methods=['GET', 'POST'])
def delete_form():
    # handle the POST request
    if request.method == 'POST':
        delete_book(request.form.get('id'))

    # otherwise handle the GET request
    return '''
           <form method="POST">
                <div><label>ID: <input type="integer" name="id"></label></div>
                <input type="submit" value="Submit">
           </form>'''

if __name__ == '__main__':
    app.run()