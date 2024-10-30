from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Get all todo items
@router.get("/todos/", response_model=list[schemas.Todo])
def read_todos(db: Session = Depends(get_db)):
    todos = crud.get_todos(db)
    return todos

# Create a new todo item
@router.post("/todos/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

# Update a todo item
@router.put("/todos/{todo_id}", response_model=schemas.Todo)
def update_todo(todo_id: int, todo_update: schemas.TodoUpdate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, todo_update)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Delete a todo item
@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"detail": "Todo deleted"}

