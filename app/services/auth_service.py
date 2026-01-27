import jwt
from werkzeug.security import check_password_hash
from app.data.users import users
from datetime import datetime, timedelta
from app.config import SECRET_KEY, JWT_EXPIRED_SECONDS
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token


def login_user(data):
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return None
    
    token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "roles": user.roles
        })

    return token

