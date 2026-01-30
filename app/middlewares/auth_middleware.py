from flask_jwt_extended import get_jwt, jwt_required
from flask import jsonify
from functools import wraps


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorated(*args, **kwargs):
            claims = get_jwt()
            user_roles = claims.get("roles")

            if user_roles != role:
                return jsonify({
                    "message": "You do not have permission to access this resource"
                }), 403
            
            return fn(*args, **kwargs)
        return decorated
    return wrapper