from flask import blueprints
from app.controllers.auth_controller import login, refresh, logout_user

auth_bp = blueprints.Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/refresh', methods=['POST'])(refresh)
auth_bp.route('/logout', methods=['POST'])(logout_user)