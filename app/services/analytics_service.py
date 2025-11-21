from sqlalchemy.orm import Session
from app.models import User, Matching
from sqlalchemy import func
import httpx
from collections import Counter

# def get_user_insights(db: Session):
#     data = db.query(User.role, func.count(User.id)).group_by(User.role).all()
#     return [{"role": role, "count": count} for role, count in data]
POSTINGS_API = "http://postings-service/api/v1/postings"
USERS_API = "http://users-service/api/v1/users"

async def get_user_insights():
    async with httpx.AsyncClient() as client:
        response = await client.get(USERS_API)

    if response.status_code != 200:
        raise Exception("Failed to fetch users")

    users = response.json()   

    # Count by role
    role_counts = Counter([user["role"] for user in users])

    # Format output
    return [
        {"role": role, "count": count}
        for role, count in role_counts.items()
    ]

# def get_matching_insights(db: Session):
#     data = db.query(Matching.status, func.count(Matching.id)).group_by(Matching.status).all()
#     return [{"status": status, "count": count} for status, count in data]

async def get_volunteers_registered_for_posting(posting_id: int):
    async with httpx.AsyncClient() as client:

        # Fetch posting details
        posting_res = await client.get(f"{POSTINGS_API}/{posting_id}")
        if posting_res.status_code != 200:
            raise Exception(f"Posting {posting_id} not found")

        posting_data = posting_res.json()

        volunteer_ids = posting_data.get("volunteersRegistered", [])

        # If no volunteers registered
        if not volunteer_ids:
            return {
                "postingId": posting_id,
                "postingTitle": posting_data.get("title"),
                "totalVolunteersRegistered": 0,
                "volunteers": []
            }

        # Fetch each volunteer details
        volunteer_details = []
        for vid in volunteer_ids:
            user_res = await client.get(f"{USERS_API}/{vid}")
            if user_res.status_code == 200:
                volunteer_details.append(user_res.json())
            else:
                volunteer_details.append({"id": vid, "error": "User not found"})

        # Build final analytics response
        return {
            "postingId": posting_id,
            "postingTitle": posting_data.get("title"),
            "totalVolunteersRegistered": len(volunteer_details),
            "volunteers": volunteer_details
        }