from fastapi import APIRouter
from app.pinpoints.views import router

API_STR = "/api"

sneakers_router = APIRouter(prefix=API_STR)
sneakers_router.include_router(router)
