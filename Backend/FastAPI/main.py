from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "¡Hola FastAPI.!"

# Url local: http://127.0.0.1:8000

@app.get("/url")
async def root():
    return {"url_curso":"https://mouredev.com/python"}

# Url local (/url): http://127.0.0.1:8000/url

# Inicia el server: uvicorn Backend.FastAPI.main:app --reload
# Detener el server: CTRL+C

#Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc