from flask import request, jsonify
from sqlalchemy import Null
from app.services.auth_service import login_user, refresh_token, logout
from flask_jwt_extended import jwt_required

def login():
    data = request.get_json()

    if data.get("username") == None:
        return jsonify({
            "status": "fail",
            "message": "Username is required"
        }), 400
    if data.get("password") == None:\
        return jsonify({
            "status": "fail",
            "message" : "Password is required"
        }), 400

    token = login_user(data)

    if not token:
        return jsonify({
            "status": "fail",
            "message": f"Invalid Username or Password"
        }), 401
    
    return jsonify({
        "status": "success",
        "message": "login successfull",
        "token": token["access_token"],
        "refresh_token" : token["refresh_token"]
    }), 200

def refresh():
    return refresh_token()

def logout_user():
    @jwt_required()
    def inner():
        logout()

        return {
            "status": "success",
            "message": "Logout Successfull"
        }, 200

    return inner()