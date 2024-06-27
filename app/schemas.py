from pydantic import BaseModel, AnyUrl


class BaseMeme(BaseModel):
    title: str
    description: str | None = None
    image_url: AnyUrl


class MemeCreate(BaseMeme):
    pass


class MemeUpdate(BaseMeme):
    pass


class MemeFromDBBase(BaseMeme):
    id: int

    class Config:
        from_attributes = True


class Meme(MemeFromDBBase):
    pass
