from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.analytics_service import get_user_insights, get_matching_insights

router = APIRouter(prefix="/api/v1/admin/analytics", tags=["Analytics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/user-insights")
def user_insights(db: Session = Depends(get_db)):
    return {"data": get_user_insights(db)}

@router.get("/matching-insights")
def matching_insights(db: Session = Depends(get_db)):
    return {"data": get_matching_insights(db)}
