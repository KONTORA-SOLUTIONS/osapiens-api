import os
from fastapi import FastAPI, APIRouter
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

from app.images import router as image_router
from app.core.main_router import router as main_router
from app.auth import router as auth_router
from app.users import router as users_router
from app.pinpoints import router as pinpoints_router
from app.core.logger import init_logging

load_dotenv(".env")

root_router = APIRouter()


app = FastAPI(title="osapiens API")
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

app.include_router(image_router)
app.include_router(main_router)
app.include_router(root_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(auth_router)
app.include_router(pinpoints_router)

init_logging()

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
