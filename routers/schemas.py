from datetime import datetime
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
        
class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    caption: str
    creator_id: str
    
class User(BaseModel):
    username: str
    class Config():
        orm_mode = True
    
class PostDisplay:
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    