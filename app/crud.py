from sqlalchemy.orm import Session
from app import models, schemas

def get_todos(db: Session):
    return db.query(models.TodoItem).all()

def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.TodoItem(title=todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo:
        db_todo.title = todo_update.title
        db_todo.description = todo_update.description
        db_todo.completed = todo_update.completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.TodoItem).filter(models.TodoItem.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
