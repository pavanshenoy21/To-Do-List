from sqlalchemy.orm import Session
import models, schemas

def create_todo(db: Session, todo: schemas.CreateEntry):
    db_todo=models.ToDo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session):
    return db.query(models.ToDo).all()

def mark_complete(db : Session, todo_id:int):
    todo= db.query(models.ToDo).filter(models.ToDo.id==todo_id).first()
    if todo:
        todo.completed= True
        db.commit()

    return todo

def update_status( todo_id : int , db : Session , status_update : schemas.StatusUpdate):
    todo= db.query(models.ToDo).filter(models.ToDo.id==todo_id).first()
    if todo:
        todo.Status= status_update.Status
        db.commit()
        db.refresh(todo)

    return todo

def delete_status(todo_id : int , db : Session,):
    todo = db.query(models.ToDo).filter(models.ToDo.id==todo_id).first()
    db.delete(todo)
    db.commit()
    return todo