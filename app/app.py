from fastapi import FastAPI
from app.users.routes import router as users

app = FastAPI()
app.include_router(users, tags=["Users"], prefix="/user")


@app.on_event('startup')
async def startup():
    pass


@app.on_event('shutdown')
async def shutdown():
    pass


@app.get('/')
async def main():
    return "Hello"
