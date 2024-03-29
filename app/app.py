from fastapi import FastAPI
from app.users.routes import router as users
from app.exchanges.routes import router as exchanges

app = FastAPI(
    title="bankApi",
    redoc_url="",
    # docs_url="",
    openapi_url="/api/v1/openapi.json",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)
# app.include_router(users, tags=["Users"], prefix="/user")
app.include_router(exchanges, tags=["Exchanges"], prefix="/exchange")


@app.on_event('startup')
async def startup():
    pass


@app.on_event('shutdown')
async def shutdown():
    pass


@app.get('/', tags=["Main page"])
async def index():
    return "Hello"
