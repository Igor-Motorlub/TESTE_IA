"""FastAPI application for task management."""

from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import engine, get_db

app = FastAPI(
    title="Task Management API",
    description="API para gerenciamento de tarefas com FastAPI, SQLite e SQLAlchemy.",
    version="1.0.0",
)


@app.on_event("startup")
def startup() -> None:
    """Create database tables when the application starts."""
    models.Base.metadata.create_all(bind=engine)


@app.get("/", response_model=schemas.RootResponse)
def read_root() -> dict[str, str]:
    """Return a welcome message for the API."""
    return {"message": "Bem-vindo a Task Management API"}


@app.post(
    "/tasks/",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"],
)
def create_task(
    task: schemas.TaskCreate,
    db: Session = Depends(get_db),
) -> models.Task:
    """Create a new task."""
    db_task = models.Task(
        title=task.title,
        description=task.description,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=list[schemas.TaskResponse], tags=["Tasks"])
def list_tasks(
    skip: int = 0,
    limit: int = 10,
    completed: Optional[bool] = None,
    db: Session = Depends(get_db),
) -> list[models.Task]:
    """List tasks with optional pagination and completion filter."""
    query = db.query(models.Task)
    if completed is not None:
        query = query.filter(models.Task.completed == completed)
    return query.offset(skip).limit(limit).all()


@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)) -> models.Task:
    """Get a task by its identifier."""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse, tags=["Tasks"])
def update_task(
    task_id: int,
    task_update: schemas.TaskUpdate,
    db: Session = Depends(get_db),
) -> models.Task:
    """Update an existing task."""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    if update_data:
        db.commit()
        db.refresh(task)
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)) -> Response:
    """Delete a task by its identifier."""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
