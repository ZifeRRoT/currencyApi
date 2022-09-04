from fastapi import FastAPI
from users.routes import router as users
from exchanges.routes import router as exchanges

app = FastAPI()
# app.include_router(users, tags=["Users"], prefix="/user")
app.include_router(exchanges, tags=["Exchanges"], prefix="/exchange")


@app.on_event('startup')
async def startup():
    pass


@app.on_event('shutdown')
async def shutdown():
    pass


@app.get('/')
async def main():
    return "Hello"
