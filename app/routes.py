from fastapi import APIRouter, Depends
from app.models import get_db
from sqlalchemy.orm import Session
from app import crud
from app.schemas import PostCreate

router = APIRouter()


@router.post("", status_code=201)
async def get_posts(request: PostCreate,db: Session = Depends(get_db)):
    return crud.create_post(db,request)