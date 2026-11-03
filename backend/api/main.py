from fastapi import FastAPI

app = FastAPI(title = "포켓몬 스토리 공략 도우미 API")

@app.get("/")
def hello():
    return {"message":"안녕, 포켓몬 서버!!"}