from flask import Blueprint
from app.controllers.book_controller import create_book, get_all_books, getBookByid, editBookById, deleteBookById


book_bp = Blueprint('book_bp', __name__)

book_bp.route('/books', methods=['POST'])(create_book)
book_bp.route('/books', methods=['GET'])(get_all_books)
book_bp.route('/books/<book_id>', methods=['GET'])(getBookByid)
book_bp.route('/books/<book_id>', methods=['PUT'])(editBookById)
book_bp.route('/books/<book_id>', methods=['DELETE'])(deleteBookById)

