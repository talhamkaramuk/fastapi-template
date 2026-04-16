from fastapi import FastAPI

from app.api.v1.routers.health import router as health_router

app = FastAPI(
    title="FastAPI Template",
    version="1.0.0",
)

# Router'ları ekle
app.include_router(health_router, prefix="/api/v1")
