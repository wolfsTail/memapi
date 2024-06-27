from sqlalchemy.orm import Session
from app import models, schemas


def get_meme(db: Session, item_id: int):
    return db.query(models.Meme).filter(models.Meme.id == item_id).first()

def get_memes(db: Session, limit: int = 10):
    return db.query(models.Meme).limit(limit).all()

def create_meme(db: Session, meme: schemas.MemeCreate):
    db_meme = models.Meme(**meme.model_dump())
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme

def update_meme(db: Session, item_id: int, meme: schemas.MemeUpdate):
    db_meme = db.query(models.Meme).filter(models.Meme.id == item_id).first()
    if db_meme:
        for key, value in meme.model_dump().items():
            setattr(db_meme, key, value)
        db.commit()
        db.refresh(db_meme)
    return db_meme

def delete_meme(db: Session, item_id: int):
    db_meme = db.query(models.Meme).filter(models.Meme.id == item_id).first()
    if db_meme:
        db.delete(db_meme)
        db.commit()
    return db_meme
