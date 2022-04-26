from pydantic import BaseModel, Field
import datetime as dt


class PageOut(BaseModel):
    content: str
    downlaoded_date: dt.datetime = Field(default_factory=dt.datetime.now)


class GetPage(BaseModel):
    url: str = Field(
        default="https://pokeapi.co/api/v2/pokemon-form/151/"  # just for that assignment
    )


class InfoMessage(BaseModel):
    receiver: str
