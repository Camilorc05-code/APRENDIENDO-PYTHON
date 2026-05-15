from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "80b3a09b367733cd69fa825f53df84ce1c7d9359a76c025e6bb0ba9c1a2f70d8"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool

class UserDB(User):
    password: str

users_db = {
    "Camilo": {
        "username": "Camilo",
        "full_name": "Camilo Rodriguez",
        "email": "camilo@gmail.com",
        "disable": False,
        "password": "$2a$12$GQwuSPQDeqP3BLMjCFntQOBQUdEbgVmYj4rAQDKZ.TX7wWGcuT1jG"
    },
    "Felipe": {
        "username": "Felipe",
        "full_name": "Felipe Rodriguez 2",
        "email": "felipe@gmail.com",
        "disable": True,
        "password": "$2a$12$d8828iystAUjzN19xs.3oehPpcO.1IOuIBtLwd/aaSXVTNNADMXcG"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    
def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):
  
  exception = HTTPException(
            status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autentificación invalidas", 
            headers={"WWW-Authenticate": "Bearer"})

  try:
    username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
    if username is None:
       raise exception

  except JWTError:
    raise exception
  
  return search_user(username)
    
async def current_user(user: User = Depends(auth_user)): 
    if user.disable:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo")

    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
   user_db = users_db.get(form.username)
   if not user_db:
       raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
   
   user = search_user_db(form.username)

   if not crypt.verify(form.password, user.password): 
       raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
   
   expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)
   
   access_token = {"sub": user.username, 
                   "exp": int(expire.timestamp())}
   
   return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user