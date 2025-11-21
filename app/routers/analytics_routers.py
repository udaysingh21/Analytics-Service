from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.analytics_service import get_user_insights, get_matching_insights, get_volunteers_registered_for_posting

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

@router.get("/volunteers-per-posting/{posting_id}")
async def volunteers_for_posting(posting_id: int):
    return await get_volunteers_registered_for_posting(posting_id)