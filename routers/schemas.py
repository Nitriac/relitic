import email
from email.mime import base
from lib2to3.pytree import Base
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    
class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True
    