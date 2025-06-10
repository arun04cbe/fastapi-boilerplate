"""FastAPI boilerplate main file."""

import uvicorn
from fastapi import FastAPI

from src.config import settings

app = FastAPI(
    title="FastAPI boilerplate",
    version="0.1.0",
)


@app.get("/")
async def status() -> dict:
    """Health check endpoint.

    Returns:
        dict: A dictionary with the status of the service.
    """
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
    )
