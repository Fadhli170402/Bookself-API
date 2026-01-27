from flask import Flask
from app.routes.book_routes import book_bp
from app.routes.auth_routes import auth_bp
from app.routes.users import user_bp
from app.extensions import db, migrate, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(book_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    
    return app