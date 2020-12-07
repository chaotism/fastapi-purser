from fastapi import APIRouter

from app.routers.health.endpoints import application_status

api_router = APIRouter()
api_router.include_router(application_status.router, tags=["health"])
