from pydantic import BaseModel, Field

class ItemIn(BaseModel):
    name: str = Field(max_length=128)
    description: str = Field(max_length=500)
    price: float = Field(gt=0, le=100000)


class Item(BaseModel):
    id: int
    name: str = Field(max_length=128)
    description: str = Field(max_length=500)
    price: float = Field(gt=0, le=100000)
