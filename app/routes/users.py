from flask import Blueprint
from app.controllers.user_controller import create_user, editUserById,get_all_users, get_user_by_id,deleteUser

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/users', methods=['POST'])(create_user)
user_bp.route('/users', methods=['GET'])(get_all_users)
user_bp.route('/users/<user_id>', methods=['GET'])(get_user_by_id)
user_bp.route('/users/<user_id>', methods=['PUT'])(editUserById)
user_bp.route('/users/<user_id>', methods=['DELETE'])(deleteUser)