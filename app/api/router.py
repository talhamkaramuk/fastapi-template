from app.api.v1.routers import health
from fastapi import APIRouter

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health.router, prefix="/health", tags=["Health"])
