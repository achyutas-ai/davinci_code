from fastapi import APIRouter, Query
from app.models.model import Item

router = APIRouter(prefix="/v1")

@router.get("/users")
async def users():
    return {"fruits":["apple","orang"]}

@router.post("/items", status_code=201)
async def create_item(item: Item):
    return {"created":item}

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id":item_id, "item":item}


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id":item_id}

@router.get("/search")
async def search(query: str = Query(...,min_length=5,max_length=20)):
    return {"query":query}
