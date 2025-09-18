from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Task, TaskStatus
from .schemas import TaskCreate, TaskUpdate


async def create_task(db: AsyncSession, task_in: TaskCreate) -> Task:
    db_task = Task(title=task_in.title, description=task_in.description, status=TaskStatus(task_in.status))
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def get_task(db: AsyncSession, task_id: int) -> Optional[Task]:
    return await db.get(Task, task_id)


async def list_tasks(db: AsyncSession, skip: int = 0, limit: int = 10, status: Optional[str] = None) -> List[Task]:
    q = select(Task).order_by(Task.created_at.desc()).offset(skip).limit(limit)
    if status:
        q = q.where(Task.status == TaskStatus(status))
    res = await db.execute(q)
    return res.scalars().all()


async def update_task(db: AsyncSession, task_id: int, task_in: TaskUpdate) -> Optional[Task]:
    db_task = await db.get(Task, task_id)
    if not db_task:
        return None
    for k, v in task_in.dict(exclude_unset=True).items():
        if k == "status" and v is not None:
            setattr(db_task, k, TaskStatus(v))
        else:
            setattr(db_task, k, v)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def delete_task(db: AsyncSession, task_id: int) -> bool:
    db_task = await db.get(Task, task_id)
    if not db_task:
        return False
    await db.delete(db_task)
    await db.commit()
    return True
