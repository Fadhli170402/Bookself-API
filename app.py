from flask import Flask
from app.extensions import db
from app.config import SQLALCHEMY_DATABASE_URI
from flask_migrate import Migrate
from app.routes.book_routes import book_bp
from app.routes.auth_routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate.init_app(app, db)

    app.register_blueprint(book_bp)
    app.register_blueprint(auth_bp) 

    return app

app = create_app()
if __name__ == '__main__':
    app.run(debug=True)
    