import uvicorn
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    uvicorn.run("app.app:app", reload=True, port=80)
