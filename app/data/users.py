# UNUSED FILE: This file is no longer used. Users are now stored in the database (User model).
# You can safely delete this file if you are sure you don't need the static data.

from werkzeug.security import generate_password_hash

users = [
    {
        "id": "A1",
        "username": "admin",
        "password": generate_password_hash("admin123")
    }
]