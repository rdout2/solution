from datetime import datetime
from app.db import db

class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Enum('Wishlist', 'Applied', 'Interview', 'Offer', 'Rejected', name='status_enum'), nullable=False)
    date_applied = db.Column(db.Date, nullable=True)
    job_board = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "company": self.company,
            "status": self.status,
            "date_applied": self.date_applied.isoformat() if self.date_applied else None,
            "job_board": self.job_board,
            "location": self.location,
            "notes": self.notes,
            "created_at": self.created_at.isoformat()
        }
