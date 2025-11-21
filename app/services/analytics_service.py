from sqlalchemy.orm import Session
from app.models import User, Matching
from sqlalchemy import func
import httpx
from collections import Counter

# def get_user_insights(db: Session):
#     data = db.query(User.role, func.count(User.id)).group_by(User.role).all()
#     return [{"role": role, "count": count} for role, count in data]
POSTINGS_API = "http://localhost:8082/api/v1/postings"
USERS_API = "http://localhost:8081/api/v1/users"

async def get_user_insights(token: str):
    async with httpx.AsyncClient() as client:
        headers = {"Authorization": f"Bearer {token}"}

        response = await client.get(USERS_API, headers=headers)

    if response.status_code != 200:
        raise Exception("Failed to fetch users")

    users = response.json()

    role_counts = Counter([user["roleType", "UNKNOWN"] for user in users])

    return [
        {"role": role, "count": count}
        for role, count in role_counts.items()
    ]


# def get_matching_insights(db: Session):
#     data = db.query(Matching.status, func.count(Matching.id)).group_by(Matching.status).all()
#     return [{"status": status, "count": count} for status, count in data]

async def get_volunteers_registered_for_posting(posting_id: int, token: str):
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:

        # Fetch posting details (secured)
        posting_res = await client.get(
            f"{POSTINGS_API}/{posting_id}",
            headers=headers
        )
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

        # Fetch each volunteer details (secured)
        volunteer_details = []
        for vid in volunteer_ids:
            user_res = await client.get(
                f"{USERS_API}/{vid}",
                headers=headers
            )

            if user_res.status_code == 200:
                volunteer_details.append(user_res.json())
            else:
                volunteer_details.append({"id": vid, "error": "User not found"})

        # Return final analytics response
        return {
            "postingId": posting_id,
            "postingTitle": posting_data.get("title"),
            "totalVolunteersRegistered": len(volunteer_details),
            "volunteers": volunteer_details
        }