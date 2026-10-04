from pydantic import BaseModel, ConfigDict, Field

class ProjectCreate(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    name: str = Field(
        min_length=3,
        max_length=120,
    )
    description: str | None = Field(
        default=None,
        max_length=500,
    )

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    status: str