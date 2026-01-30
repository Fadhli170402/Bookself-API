from flask import request, jsonify
from app.services.auth_service import login_user, refresh_token


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
        "token": token["access_token"],
        "refresh_token" : token["refresh_token"]
    }), 200

def refresh():
    return refresh_token()