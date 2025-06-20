from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import SessionLocal
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# Example Pydantic model - adjust to your table columns
class Item(BaseModel):
    id: int
    name: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/", response_model=list[Item])
def read_items(db: Session = Depends(get_db)):
    result = db.execute("SELECT id, name FROM users;")
    return [Item(id=row.id, name=row.name) for row in result]