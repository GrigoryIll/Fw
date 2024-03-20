from fastapi import APIRouter
from db import users
from models.user import User, UserIn
from db import database

router = APIRouter()


@router.post("/users/", response_model=UserIn)
async def create_user(user: UserIn):
    query = users.insert().values(
    name=user.name,
    surname=user.surname,
    email=user.email,
    password=user.password)
    await database.execute(query)
    return user

@router.get("/users/", response_model=list[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)

@router.put("/users/{user_id}", response_model=UserIn)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id ==
    user_id).values(**new_user.model_dump())
    await database.execute(query)
    return new_user

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


