from fastapi import FastAPI
from app.routers.analytics_routers import router
app = FastAPI(title="Analytics Service")

app.include_router(router)
