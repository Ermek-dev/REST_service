from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


# Используем Enum, чтобы Pydantic автоматически сериализовал в строку
class StatusEnum(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[StatusEnum] = StatusEnum.todo


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None


class TaskRead(TaskBase):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
