from fastapi import APIRouter
from db import items, database
from models.item import Item, ItemIn

router = APIRouter()


@router.post("/items/", response_model=ItemIn)
async def create_item(item: ItemIn):
    query = items.insert().values(
    name=item.name,
    description=item.description,
    price=item.price)
    await database.execute(query)
    return item

@router.get("/items/", response_model=list[Item])
async def read_items():
    query = items.select()
    return await database.fetch_all(query)

@router.put("/items/{item_id}", response_model=ItemIn)
async def update_item(item_id: int, new_item: ItemIn):
    query = items.update().where(items.c.id ==
    item_id).values(**new_item.model_dump())
    await database.execute(query)
    return new_item

@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}


