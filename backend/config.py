from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from slowapi import Limiter
from slowapi.util import get_remote_address
import os

#Load variables
load_dotenv()

GOOGLE_CLIENT_ID           = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET       = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_SERVER_METADATA_URL = os.getenv("GOOGLE_SERVER_METADATA_URL")
GOOGLE_OAUTH2_USERINFO     = os.getenv("GOOGLE_OAUTH2_USERINFO")

MICROSOFT_CLIENT_ID     = os.getenv("MICROSOFT_CLIENT_ID")
MICROSOFT_CLIENT_SECRET = os.getenv("MICROSOFT_CLIENT_SECRET")

LOG_FOLDER_PATH   = os.getenv("LOG_FOLDER_PATH")
DEV_MODE          = os.getenv("DEV_MODE")
MYSQL_URI         = os.getenv("MYSQL_URI")
JWT_SECRET        = os.getenv("JWT_SECRET")
ALGORITHM         = os.getenv("ALGORITHM")

ALLOWED_ORIGINS   = os.getenv("ALLOWED_ORIGINS")
ALLOWED_METHODS = ["*"]
ALLOWED_HEADERS = ["*"]
SESSION_SECRET_KEY = os.getenv("SESSION_SECRET_KEY")
FRONTEND_BASE_URL = os.getenv("FRONTEND_BASE_URL")

# SQLAlchemy setup
devMode = False
if MYSQL_URI:
    devMode = True
engine = create_async_engine(MYSQL_URI, echo=devMode)
localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
base = declarative_base()

async def get_db():
    async with localSession() as session:
        yield session

limiter = Limiter(key_func=get_remote_address)


