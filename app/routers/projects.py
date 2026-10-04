from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.projects import (
    ProjectCreate,
    ProjectResponse,
)


router = APIRouter(
    prefix="/projects",
    tags=["projects"],
)

def get_default_status() -> str:
    return "active"

DefaultStatusDep = Annotated[
    str,
    Depends(get_default_status),
]


@router.post(
        "", 
        response_model=ProjectResponse,
        status_code=201,
        )
def create_project(
    request: ProjectCreate,
    default_status: DefaultStatusDep,
) -> ProjectResponse:
    return ProjectResponse(
        id=1,
        name=request.name,
        description=request.description,
        status="active",
    )

@router.get(
    "",
    response_model=list[ProjectResponse],
)
def list_projects(
    status: str | None = None,
) -> list[ProjectResponse]:
    projects = [
        ProjectResponse(
            id=1,
            name="API Course",
            description=None,
            status="active",
        ),
        ProjectResponse(
            id=2,
            name="Legacy Project",
            description=None,
            status="inactive",
        ),
    ]

    if status is None:
        return projects

    return [
        project
        for project in projects
        if project.status == status
    ]


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
)
def read_project(
    project_id: int,
) -> ProjectResponse:
    if project_id != 1:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )
    
    return ProjectResponse(
        id=project_id,
        name="API Course",
        description=None,
        status="active",
    )