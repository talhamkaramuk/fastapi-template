from app.api.router import api_router
from fastapi import FastAPI

app = FastAPI(
    title="YOUR APP NAME",
    version="1.0.0",
)

app.include_router(api_router)
