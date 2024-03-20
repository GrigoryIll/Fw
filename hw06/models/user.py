from pydantic import BaseModel, EmailStr, Field

class UserIn(BaseModel):
    name: str = Field(max_length=128)
    surname: str = Field(max_length=128)
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=8)

class User(BaseModel):
    id: int
    name: str = Field(max_length=128)
    surname: str = Field(max_length=128)
    email: EmailStr = Field(max_length=128)
