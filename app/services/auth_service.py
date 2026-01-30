from flask import jsonify
from werkzeug.security import check_password_hash
from app.data.users import users
from datetime import datetime, timedelta
from app.config import SECRET_KEY, JWT_EXPIRED_SECONDS
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt, get_jwt_identity, jwt_required


def login_user(data):
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return None
    
    access_token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "roles": user.roles
        })

    refresh_token = create_refresh_token(
        identity=str(user.id)
    )

    return {
       "access_token": access_token,
       "refresh_token": refresh_token
    }

def refresh_token():
    @jwt_required(refresh=True)
    def inner():
        user_id = get_jwt_identity()
        claims = get_jwt()

        new_access_token = create_access_token(
            identity=str(user_id),
            additional_claims={
                "roles": claims.get("roles")
            }
        )

        return jsonify({
            "access_token": new_access_token
        }), 200
    
    return inner()