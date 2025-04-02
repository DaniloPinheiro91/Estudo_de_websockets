# python venv.venv
# Set-ExecutionPolicy - Scope Process -ExecutionPolicy Bypass - corrigir erro
#.venv\Script\activate - ativa o ambiente virtual
#uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def home():
    
    return {'Message: ': 'Hello World'}
