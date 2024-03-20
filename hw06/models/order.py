from pydantic import BaseModel, Field

class OrderIn(BaseModel):
    user_id: int
    item_id: int
    create_date: str
    status: str = Field(max_length=32)

class Order(BaseModel):
    id: int
    user_id: int
    item_id: int
    create_date: str
    status: str = Field(max_length=32)