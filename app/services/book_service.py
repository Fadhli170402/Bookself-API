from app.models import Book
from app.extensions import db
from datetime import datetime
import nanoid

def add_book(data):
    date = datetime.now().isoformat()

    book = Book(
        id= nanoid.generate(size=8),
        name = data["name"],
        year = data["year"],
        author = data["author"],
        summary = data["summary"],
        publisher = data["publisher"],
        page_count = data["page_count"],
        read_page = data["read_page"],
        reading = data["reading"]
    )
    db.session.add(book)
    db.session.commit()
    return book

def fetch_all_book():
    return Book.query.all()

def get_book_by_id(book_id):
    return Book.query.get(book_id)

def edit_book_by_id(book_id, data):
    book = Book.query.get(book_id)
    if book:
        book.name = data.get("name", book.name)
        book.year = data.get("year", book.year)
        book.author = data.get("author", book.author)
        book.summary = data.get("summary", book.summary)
        book.publisher = data.get("publisher", book.publisher)
        book.page_count = data.get("page_count", book.page_count)
        book.read_page = data.get("read_page", book.read_page)
        book.reading = data.get("reading", book.reading)
        book.updated_at = datetime.now()
        
        db.session.commit()
        return book.to_dict()
    return None


def delete_book_by_id(book_id):
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return True
    return False