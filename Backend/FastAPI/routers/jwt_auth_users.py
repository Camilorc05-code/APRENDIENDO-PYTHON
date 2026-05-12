from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt 
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1

app = FastAPI()

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

@app.post("/login")
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
                   "exp": expire.isoformat()}
   
   return {"access_token": access_token, "token_type": "bearer"}