# Analytics-Service

## Analytics Service – FastAPI

This is the Analytics Microservice for aggregating data from the Users and Postings services.
It exposes secure admin analytics endpoints that require JWT authentication.

## Project Structure

```
ANALYTICS-SERVICE/
│
├── app/
│   ├── routers/              # API route handlers
│   ├── services/             # Business logic (API calls, analytics)
│   ├── __init__.py
│   ├── config.py             # Service configuration
│   ├── database.py           # DB setup (if required)
│   ├── main.py               # FastAPI entrypoint
│   ├── models.py             # ORM models (User, Matching)
│
├── dockerfile                # Docker image setup
├── requirements.txt          # Python dependencies
├── swagger.yaml              # API documentation (OpenAPI spec)
└── README.md                 # Project documentation
```

## Running the Service

1. Install dependencies
```
pip install -r requirements.txt
```

2. Start FastAPI
```
uvicorn app.main:app --reload --port 8005
```

3. Access Swagger UI
http://localhost:8005/docs

## Authentication

All analytics APIs require a JWT Token.

Send token in the request header:

Authorization: Bearer <JWT_TOKEN>

## API Endpoints

1. User Insights API
Endpoint
```
GET /api/v1/admin/analytics/user-insights
```

Description

Fetches all users from the Users microservice and returns the count of users based on their roles
(Volunteer, Corporate, NGO, Admin, etc.)

Headers
```
Authorization: Bearer <JWT_TOKEN>
```

Sample Response:
```
[
  { "role": "VOLUNTEER", "count": 42 },
  { "role": "NGO", "count": 5 },
  { "role": "ADMIN", "count": 3 },
  { "role": "CORPORATE", "count": 12 }
]
```

2. Volunteers Registered for a Posting
Endpoint
```
GET /api/v1/admin/analytics/posting/{posting_id}/volunteers
```

Description

Fetches:

- Posting details

- List of volunteers registered for the posting

- Full volunteer profiles (pulled from Users API)

Headers
```
Authorization: Bearer <JWT_TOKEN>
```

Sample Response
```
{
  "postingId": 1,
  "postingTitle": "Beach Cleanup Drive",
  "totalVolunteersRegistered": 2,
  "volunteers": [
    {
      "id": 2,
      "name": "John",
      "roleType": "VOLUNTEER"
    },
    {
      "id": 3,
      "name": "Aditi",
      "roleType": "VOLUNTEER"
    }
  ]
}
```

## Docker

Build
```
docker build -t analytics-service .
```

Run
```
docker run -p 8005:8005 analytics-service
```
