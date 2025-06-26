from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from itsdangerous import URLSafeTimedSerializer
from config import (SESSION_SECRET_KEY, get_db, GOOGLE_CLIENT_ID, 
                    GOOGLE_CLIENT_SECRET, MICROSOFT_CLIENT_ID, MICROSOFT_CLIENT_SECRET)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.models import User
from functions.utils import create_access_token
from passlib.hash import bcrypt
from functions.schemas import CodePayload, LoginRequest
import httpx
import jwt

router = APIRouter()

serializer = URLSafeTimedSerializer(SESSION_SECRET_KEY)
           
@router.post("/login")
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.username == data.username))
    user = result.scalar_one_or_none()
    if not user or not user.hashed_password or not bcrypt.verify(data.password, user.hashed_password):
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
async def google_callback(payload: CodePayload, db: AsyncSession = Depends(get_db)):
    code = payload.code
    token_url = "https://oauth2.googleapis.com/token"
    redirect_uri = "http://localhost:3000/oauth/google/callback"

    data = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(token_url, data=data)
            resp.raise_for_status()
            tokens = resp.json()
            id_token = tokens["id_token"]
            id_info = jwt.decode(id_token, options={"verify_signature": False})
            email = id_info["email"]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"OAuth failed: {str(e)}")

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()

    if not user:
        new_user = User(email=email, oauth_provider="google", status=1)
        db.add(new_user)
        await db.commit()

    token = create_access_token({"sub": email})
    return {"token": token}

@router.get("/auth/microsoft")
def microsoft_auth():
    redirect_uri = "http://localhost:3000/oauth/microsoft/callback"
    url = (
        f"https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id={MICROSOFT_CLIENT_ID}"
        f"&response_type=code"
        f"&redirect_uri={redirect_uri}"
        f"&response_mode=query"
        f"&scope=openid%20email%20profile%20User.Read"
    )
    return RedirectResponse(url)

@router.post("/auth/microsoft/callback")
async def microsoft_callback(payload: CodePayload, db: AsyncSession = Depends(get_db)):
    code = payload.code
    print(f"Incoming Microsoft OAuth code: {payload.code}")
    token_url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
    redirect_uri = "http://localhost:3000/oauth/microsoft/callback"
    data = {
        "client_id": MICROSOFT_CLIENT_ID,
        "client_secret": MICROSOFT_CLIENT_SECRET,
        "code": code,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.post(token_url, data=data, headers=headers)
            resp.raise_for_status()
            tokens = resp.json()
            access_token = tokens["access_token"]

            userinfo_resp = await client.get(
                "https://graph.microsoft.com/v1.0/me",
                headers={"Authorization": f"Bearer {access_token}"}
            )
            userinfo_resp.raise_for_status()
            userinfo = userinfo_resp.json()
            
            email = userinfo.get("userPrincipalName") or userinfo.get("mail")
            if not email:
                raise HTTPException(status_code=400, detail="No email returned from Microsoft.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Microsoft OAuth failed: {str(e)}")

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    
    if not user:
        new_user = User(email=email, oauth_provider="microsoft", status=1)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        user = new_user  # ✅ Assign it to make sure it’s used below

    token = create_access_token({"sub": user.email})
    return {"token": token}