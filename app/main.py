from fastapi import FastAPI

from app.api.v1 import meme_router


app = FastAPI(title="Meme API")
app.include_router(router=meme_router.router, prefix="/memes", tags=["memes"])


@app.get("/")
def read_root():
    return {"message": "This is root!"}
