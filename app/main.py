from fastapi import FastAPI


app = FastAPI(title="Meme API")


@app.get("/")
def read_root():
    return {"message": "This is root!"}
