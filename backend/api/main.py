from fastapi import FastAPI
from api.routers import health

app = FastAPI(title = "포켓몬 스토리 공략 도우미 API")

app.include_router(health.router)
