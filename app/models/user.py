from app.extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(8), primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable= False)
    password = db.Column(db.String(255), nullable= False)
    # role = db.Column(db.String(20), default='user')
    roles = db.Column(db.Enum('admin', 'user'), default='user')

    createdAt = db.Column(db.DateTime, default=datetime.now().isoformat())

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "roles": self.roles,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None
        }
