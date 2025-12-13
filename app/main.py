from fastapi import FastAPI
from app.api.v1.routes import router as api_router

app = FastAPI(title="FastAPI Deep Dive")

# include router modules
app.include_router(api_router)

@app.get("/users")
async def get_users():
    return {"items":["apple","banana"]}

