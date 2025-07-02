from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import base, engine, ALLOWED_HEADERS, ALLOWED_METHODS, ALLOWED_ORIGINS, limiter, SESSION_SECRET_KEY
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from starlette.middleware.sessions import SessionMiddleware
from auth import auth

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET_KEY)

#base.metadata.create_all(bind=engine)
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(base.metadata.create_all)
        
app.add_middleware(
    CORSMiddleware,
    allow_origins     = ALLOWED_ORIGINS,
    allow_credentials = True,
    allow_methods     = ALLOWED_METHODS,
    allow_headers     = ALLOWED_HEADERS 
)

app.include_router(auth.router)