from sqlalchemy.orm import Session
from app.models import User, Matching
from sqlalchemy import func

def get_user_insights(db: Session):
    data = db.query(User.role, func.count(User.id)).group_by(User.role).all()
    return [{"role": role, "count": count} for role, count in data]

def get_matching_insights(db: Session):
    data = db.query(Matching.status, func.count(Matching.id)).group_by(Matching.status).all()
    return [{"status": status, "count": count} for status, count in data]
