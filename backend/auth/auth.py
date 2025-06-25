from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from itsdangerous import URLSafeTimedSerializer
from config import SESSION_SECRET_KEY, get_db, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.models import User
from functions.utils import create_access_token
from passlib.hash import bcrypt
import httpx
import jwt

router = APIRouter()

serializer = URLSafeTimedSerializer(SESSION_SECRET_KEY)

@router.post("/login")
async def login(username: str, password: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == username))
    user = result.scalar_one_or_none()
    if not user or not user.hashed_password or not bcrypt.verify(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.email})
    
    return {"token": token}

@router.get("/auth/google")
def google_auth():
    redirect_uri = "http://localhost:3000/oauth/google/callback"
    url = (
        f"https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}"
        f"&redirect_uri={redirect_uri}"
        f"&response_type=code"
        f"&scope=openid%20email%20profile"
    )

    return RedirectResponse(url)

@router.post("/auth/google/callback")
async def google_callback(code: str, db: AsyncSession = Depends(get_db)):
    token_url = "https://oauth2.googleapis.com/token"
    redirect_uri = "http://localhost:3000/oauth/google/callback"
    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    async with httpx.AsyncClient() as client:
        resp = await client.post(token_url, data=data)
        resp.raise_for_status()
        tokens = resp.json()
        id_token = tokens["id_token"]
        id_info = jwt.decode(id_token, options={"verify_signature": False})
        email = id_info["email"]
    
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if not user:
        new_user = User(email=email, oauth_provider="google")
        db.add(new_user)
        await db.commit()
    token = create_access_token({"sub": email})
    return {"token": token}