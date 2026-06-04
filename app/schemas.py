"""Pydantic schemas for request and response payloads."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """Validate data required to create a task."""

    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)


class TaskUpdate(BaseModel):
    """Validate optional fields for updating a task."""

    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    """Serialize task data returned by the API."""

    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
