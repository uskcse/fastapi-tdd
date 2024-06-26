from fastapi import APIRouter, Depends
from app.models import get_db
from sqlalchemy.orm import Session
from app import crud
from apps.schemas import PostCreate

router = APIRouter()


@router.post("/posts")
async def get_posts(request: PostCreate,db: Session = Depends(get_db)):
    return crud.crate_post(db,request)