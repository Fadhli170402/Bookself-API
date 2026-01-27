
import json
from flask import request, jsonify
from app.services.user_service import add_user, delete_user, edit_user_by_id, fetch_all_users, fetch_user_by_id
# from app.models.user import User

def create_user():
    data = request.get_json()
    users = add_user(data)

    if not users:
        return jsonify({
            "status": "fail",
            "message": "User Could not be added"
        }), 500

    return jsonify({
        "status": "success",
        "message": "User Added Successfully",
        "data": {
            "userId" : users.id
        }
    }), 201

def get_all_users():
    users = fetch_all_users()

    if not users:
        return jsonify({
            "status": "fail",
            "message": "No User Found"
        }), 404
    
    user = [user.to_dict() for user in users]

    return jsonify({
        "status": "success",
        "data" : {
            "users": user
        }
    }), 200

def get_user_by_id(user_id):
    user = fetch_user_by_id(user_id)

    if not user:
        return jsonify({
            "status" : "fail",
            "message": "User Not Found"
        }), 404
    
    users = user.to_dict()
    return jsonify({
        "status" : "success",
        "data": {
            "users": users
        }
    }), 200

def editUserById(user_id):
    data = request.get_json()
    user = edit_user_by_id(user_id, data)

    if not data.get("username"):
        return jsonify({
            "status": "fail",
            "message": "Username is required"
        }), 400
    if not data.get("password"):
        return jsonify({
            "status": "fail",
            "message": "Password is required"
        }), 400

    if not user:
        return jsonify({
            "status": "fail",
            "message": "User Not Found"
        }), 404
    
    return jsonify({
        "status": "success",
        "message": "User Updated Successfully",
        "data": {
            "user": user
        }
    }), 200

def deleteUser(user_id):
    user = delete_user(user_id)

    if not user:
        return jsonify({
            "status": "fail",
            "message": "User not Found. Id does not exist"
        }), 404
    
    return jsonify({
        "status": "success",
        "message": "User Deleted Successfully",
    }), 200
