from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

# TODO: Get Variants from csv
Variants = Enum("Variants", {"OTE": "ote"})


class SeachForm(BaseModel):
    index: str
    query: str
    lang: str = "l1"
    variant: Variants | None = None


@app.post("/search")
async def search(form: SeachForm):
    form_data = form.model_dump()
    # TODO: Do the search with form data
    # TODO: Cache results on disk as csv file
    # TODO: Preprocess data to be rendered
    return form_data
