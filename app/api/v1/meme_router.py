from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from  app import dao, schemas
from  app.depends import get_db


router = APIRouter()


@router.get("/", response_model=list[schemas.Meme])
def read_memes(limit: int = 10, db: Session = Depends(get_db)):
    memes = dao.get_memes(db, limit=limit)
    return memes

@router.get("/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, db: Session = Depends(get_db)):
    db_meme = dao.get_meme(db, item_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme

@router.post("/", response_model=schemas.Meme)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(get_db)):
    return dao.create_meme(db=db, meme=meme)

@router.put("/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)):
    db_meme = dao.get_meme(db, item_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return dao.update_meme(db=db, item_id=meme_id, meme=meme)

@router.delete("/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(get_db)):
    db_meme = dao.get_meme(db, item_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return dao.delete_meme(db=db, item_id=meme_id)
