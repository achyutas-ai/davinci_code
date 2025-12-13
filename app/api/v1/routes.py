from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
async def users():
    return {"fruits":["appl","orang"]}

@router.post("/items")
async def create_item(item: dict):
    return {"created":item}



