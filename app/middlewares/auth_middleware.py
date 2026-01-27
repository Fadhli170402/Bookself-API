from flask_jwt_extended import get_jwt, jwt_required, get_jwt_identity
from flask import request, jsonify
from functools import wraps
from app.config import SECRET_KEY

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth_header = request.headers.get('Authorization')

#         if not auth_header:
#             return jsonify({
#                 "status": "fail",
#                 "message": "Token is Missing"
#             }), 401
        
#         try:
#             token = auth_header.split(" ")[1]
#             jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         except:
#             return jsonify({
#                 "status": "fail",
#                 "message": "Token is Invalid"
#             }), 401
        
#         return f(*args, **kwargs)
#     return decorated

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