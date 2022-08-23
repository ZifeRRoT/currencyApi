from fastapi import FastAPI
from database import database
from app.users.routes import router as users

app = FastAPI()
app.include_router(users, tags=["Users"], prefix="/user")


@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


@app.get('/')
async def main():
    return "Hello"
