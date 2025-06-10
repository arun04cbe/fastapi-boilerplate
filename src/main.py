from fastapi import FastAPI
import uvicorn
from src.config import settings

app = FastAPI(
    title="FastAPI boilerplate",
    version="0.1.0",
)


@app.get("/")
async def status():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
    )
