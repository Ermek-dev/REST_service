from fastapi import APIRouter, Depends, HTTPException, Query, status
from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
from app.database import get_db


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=schemas.TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task_endpoint(payload: schemas.TaskCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_task(db, payload)


@router.get("/", response_model=List[schemas.TaskRead])
async def list_tasks_endpoint(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    status: Optional[str] = Query(None),
    db: AsyncSession = Depends(get_db),
):
    skip = (page - 1) * per_page
    tasks = await crud.list_tasks(db, skip=skip, limit=per_page, status=status)
    return tasks


@router.get("/{task_id}", response_model=schemas.TaskRead)
async def get_task_endpoint(task_id: int, db: AsyncSession = Depends(get_db)):
    task = await crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=schemas.TaskRead)
async def update_task_endpoint(task_id: int, payload: schemas.TaskUpdate, db: AsyncSession = Depends(get_db)):
    task = await crud.update_task(db, task_id, payload)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task_endpoint(task_id: int, db: AsyncSession = Depends(get_db)):
    ok = await crud.delete_task(db, task_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Task not found")
    return
