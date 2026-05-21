from fastapi import APIRouter, HTTPException, status
from Backend.FastAPI.db.models.user import User
from Backend.FastAPI.db.schemas.user import user_schema
from Backend.FastAPI.db.client import db_cliente

router = APIRouter()

router = APIRouter(prefix="/userdb", 
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


users_list = []


@router.get("/")
async def users():
    return users_list

# Path

@router.get("/{id}")
async def user(id: int):
    return search_user(id)

# Query

@router.get("/")
async def user(id: int):
   return search_user(id)
    
@router.post("/", status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user_by_email(user.email)) == User:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
     
    user_dict = dict(user)
    del user_dict["id"]
 
    id = db_cliente.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_cliente.local.users.find_one({"_id":id}))

    return User(**new_user)

@router.put("/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index]= user
            found = True
    if not found:
        return {"Error": "No se ha actualizado el usuario"}
    else:
        return user

@router.delete("/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"Error": "No se ha eliminado el usuario"}


def search_user_by_email(email: str):

    try:
        user = db_cliente.local.users.find_one({"email": email})
        return User(**user_schema(user))
    except:
        return {"Error": "No se ha encontrado el usuario"}
    
def search_user(id: int):
    return ""