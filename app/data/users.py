from werkzeug.security import generate_password_hash

users = [
    {
        "id": "A1",
        "username": "admin",
        "password": generate_password_hash("admin123")
    }
]