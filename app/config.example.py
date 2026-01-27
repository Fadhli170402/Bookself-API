SECRET_KEY = 'your secret key here'
JWT_EXPIRED_SECONDS = 3600

DB_USER = "your_db_user"
DB_PASSWORD = ""
DB_HOST = "your_db_host"
DB_NAME = "your_db_name"

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
JWT_SECRET_KEY = 'your_jwt_secret_key_here'
SQLALCHEMY_TRACK_MODIFICATIONS = False
