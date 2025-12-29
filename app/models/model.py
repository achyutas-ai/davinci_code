from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., min_length=1, max_length=100)
    in_stock: bool = True
