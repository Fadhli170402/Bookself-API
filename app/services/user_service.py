from werkzeug.security import generate_password_hash
from app.models.user import User
from app.extensions import db
from datetime import datetime
import nanoid

def add_user(data):
    # date = datetime.now().isoformat()
    hash_password = generate_password_hash(data["password"])

    user = User(
        id = nanoid.generate(size=8),
        username = data["username"],
        password = hash_password,
        roles = data["roles"]
    )

    db.session.add(user)
    db.session.commit()
    return user

def fetch_all_users():
    return User.query.all()

def fetch_user_by_id(user_id):
    return User.query.get(user_id)

def edit_user_by_id(user_id, data):
    user = User.query.get(user_id)
    # hashed = generate_password_hash(data["password"])

    # if not data.get("username"):
    #     return {"error": "Username is required"}, 400
    # if not data.get("password"):
    #     return {"error": "Password is required"}, 400
    if user:
        user.username = data.get("username", user.username)
        user.password = generate_password_hash(data.get("password", user.password))
        
        db.session.commit()
        return user.to_dict()
    

def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False
