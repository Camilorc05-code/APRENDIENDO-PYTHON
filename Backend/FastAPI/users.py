from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Iniciar el server: uvicorn Backend.FastAPI.users:app --reload

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="Camilo", surname="Rodriguez", url="https://camilo.com", age=20),
              User(id=2, name="Felipe", surname="Sanchez", url="https://felipe.com", age=16),
              User(id=3, name="Samuel", surname="Castañeda", url="https://samuel.com", age=12)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Camilo", "surname": "Rodriguez", "url": "https://camilo.com", "age": 20},
            {"name": "Felipe", "surname": "Sanchez", "url": "https://felipe.com", "age": 16},
            {"name": "Samuel", "surname": "Castañeda", "url": "https://samuel.com", "age": 12}]

@app.get("/users")
async def users():
    return users_list

# Path

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query

@app.get("/userquery/")
async def user(id: int):
   return search_user(id)
    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:

        return list(users)[0]
    except:
        return {"Error": "No se ha encontrado el usuario"}