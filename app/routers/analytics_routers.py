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
async def user_insights(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    token = authorization.replace("Bearer ", "")

    return await get_user_insights(token)

@router.get("/matching-insights")
def matching_insights(db: Session = Depends(get_db)):
    return {"data": get_matching_insights(db)}

@router.get("/posting/{posting_id}/volunteers")
async def volunteers_for_posting(
    posting_id: int,
    authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing JWT token")

    token = authorization.replace("Bearer ", "")

    return await get_volunteers_registered_for_posting(posting_id, token)