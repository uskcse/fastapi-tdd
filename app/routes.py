from fastapi import APIRouter, Depends
from app.models import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("")
async def get_posts(db: Session = Depends(get_db)):
    pass
