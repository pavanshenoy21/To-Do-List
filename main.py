from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, crud
from db import engine, Base, get_db
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")


app= FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    
@app.post("/todos/", response_model=schemas.EntryResponse)
def create(todo : schemas.CreateEntry, db : Session= Depends(get_db)):
    return crud.create_todo(db, todo)

@app.get("/todos/", response_model=list[schemas.EntryResponse])
def read_all(db : Session=Depends(get_db)):
    return crud.get_todos(db)

@app.put("/todos/{todo_id}", response_model=schemas.EntryResponse)
def update_status(todo_id: int, status_update: schemas.StatusUpdate, db: Session = Depends(get_db)):
    todo = crud.update_status(todo_id, db, status_update)

    if not todo:
        raise HTTPException(status_code=404, detail="To Do not found")

    return todo

@app.delete("/todos/{todo_id}", response_model=schemas.EntryResponse)
def delete_entry(todo_id: int, db: Session= Depends(get_db) ):
    todo = crud.delete_status(todo_id, db)
    if not todo:
        raise HTTPException(status_code=404, detail="To Do not found")
    return todo

