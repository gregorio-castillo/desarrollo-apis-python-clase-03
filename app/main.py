from fastapi import FastAPI

from app.routers import projects
from app.schemas.projects import (
    ProjectCreate,
    ProjectResponse,
)

app = FastAPI(
    title = "Project API",
)

app.include_router(
    projects.router,
)

@app.get("/health")
def read_health():
    return {"status": "ok"}



