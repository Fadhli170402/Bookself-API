from app.extensions import db 
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.String(8), primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    year = db.Column(db.String(4), nullable = False)
    author = db.Column(db.String(30), nullable = False)
    summary = db.Column(db.Text)
    publisher = db.Column(db.String(255))
    page_count = db.Column(db.Integer)
    read_page = db.Column(db.Integer)
    reading = db.Column(db.Boolean)

    inserted_at = db.Column(db.DateTime, default = datetime.now().isoformat())
    updated_at = db.Column(db.DateTime, default = datetime.now().isoformat()) 

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "year": self.year,
            "author": self.author,
            "summary": self.summary,
            "publisher": self.publisher,
            "page_count": self.page_count,
            "read_page": self.read_page,
            "reading": self.reading,
            "inserted_at": self.inserted_at.isoformat() if self.inserted_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }