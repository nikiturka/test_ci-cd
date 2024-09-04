import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {'message': 'Hello, World'}


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)
