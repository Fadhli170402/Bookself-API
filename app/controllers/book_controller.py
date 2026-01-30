from flask import request, jsonify
from app.services.book_service import add_book, fetch_all_book, get_book_by_id, edit_book_by_id, delete_book_by_id
from app.models.book import Book
from app.middlewares.auth_middleware import role_required

# @role_required('admin')
def create_book():
    data  = request.get_json()
    result = add_book(data)

    if not result: 
        return jsonify({
            "status": "fail",
            "message": "Book Could not be added",
        }), 500
    else:
        return jsonify({
            "status": "success",
            "message": "Book added successfully",
            "data": {
                "bookId": result.id
            }
        }), 201

@role_required('user')
def get_all_books():
    data = fetch_all_book()

    if not data: 
        return jsonify({
            "status": "fail",
            "message": "No Books Found"
        }), 404

    books = [book.to_dict() for book in data]

    return jsonify({
        "status": "success",
        "data": {
            "books": books
        }
    }), 200

# @token_required
def getBookByid(book_id):
    data =  get_book_by_id(book_id)
    if not data:
        return jsonify({
            "status": "fail",
            "message": "Book Not Found, Id Not Exist"
        }), 404

    books = data.to_dict()
    return jsonify({
        "status": "success",
        "data": {
            "books": books
        }
    }), 200

# @token_required
def editBookById(book_id):
    data = request.get_json()
    book = edit_book_by_id(book_id, data)

    if not book:
        return jsonify({
            "status": "fail",
            "message": "Book not Found. Id does Not exist"
        }), 404
    else:
        # return jsonify(result), 200
        return jsonify({
            "status": "success",
            "message": "Book Updated Successfully",
            "data": {
                "book": book
            }
        }), 200

# @token_required
def deleteBookById(book_id):
    book = delete_book_by_id(book_id)

    if not book:
        return jsonify({
            "status": "fail",
            "message": "Book not Found. Id does not exist"
        }), 404
    else:
        return jsonify({
            "status": "success",
            "message": "Deleted Book successfully"
        }), 200