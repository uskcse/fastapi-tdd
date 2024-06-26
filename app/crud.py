from sqlalchemy.orm import Session
from app.models import Post
from apps.schemas import PostCreate

def create_post(db: Session, request: PostCreate):
    post = Post(** request.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post