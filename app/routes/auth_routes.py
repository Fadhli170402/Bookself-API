from flask import blueprints
from app.controllers.auth_controller import login

auth_bp = blueprints.Blueprint('auth_bp', __name__)

auth_bp.route('/login', methods=['POST'])(login)