import enum
from sqlalchemy import Column, Integer, String, Text, DateTime, Enum as SAEnum, func

from app.db import Base


class TaskStatus(enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(SAEnum(TaskStatus, name="taskstatus"), nullable=False, server_default=TaskStatus.todo.value)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
