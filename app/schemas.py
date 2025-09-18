# app/schemas.py
from pydantic import BaseModel
from typing import Optional, Literal
from datetime import datetime

StatusLiteral = Literal["todo", "in_progress", "done"]

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[StatusLiteral] = "todo"


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusLiteral] = None


class TaskRead(TaskBase):
    id: int
    created_at: datetime
    model_config = {"from_attributes": True}
