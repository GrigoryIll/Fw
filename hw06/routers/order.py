from fastapi import APIRouter
from db import orders, database
from models.order import Order, OrderIn

router = APIRouter()


@router.post("/orders/", response_model=OrderIn)
async def create_order(order: OrderIn):
    query = orders.insert().values(
    user_id=order.user_id,
    item_id=order.item_id,
    create_date=order.create_date,
    status=order.status)
    await database.execute(query)
    return order

@router.get("/orders/", response_model=list[Order])
async def read_orders():
    query = orders.select()
    return await database.fetch_all(query)

@router.put("/orders/{order_id}", response_model=OrderIn)
async def update_order(order_id: int, new_order: OrderIn):
    query = orders.update().where(orders.c.id ==
    order_id).values(**new_order.model_dump())
    await database.execute(query)
    return new_order

@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Order deleted'}


