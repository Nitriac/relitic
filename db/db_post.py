from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DbPost


def create(db: Session, request: PostBase):
    new_post = DbPost(
        
    )