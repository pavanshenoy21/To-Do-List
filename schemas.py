from pydantic import BaseModel

class CreateEntry(BaseModel):
    Title : str
    desc : str

class TodoUpdate(BaseModel):
    completed: bool

class StatusUpdate(BaseModel):
    Status: bool

class EntryResponse(BaseModel):
    id : int
    Title : str
    desc : str
    Status : bool

    class Config:
        from_attributes= True
