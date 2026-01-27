from flask import request, jsonify
from app.services.auth_service import login_user

def login():
    data = request.get_json()

    token = login_user(data)

    if not token:
        return jsonify({
            "status": "fail",
            "message": "invalid creadentials"
        }), 401
    
    return jsonify({
        "status": "success",
        "message": "login successfull",
        "token": token
    }), 200