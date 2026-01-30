from flask import blueprints
from app.controllers.auth_controller import login,refresh

auth_bp = blueprints.Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/refresh', methods=['POST'])(refresh)