from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

from static import index
from service.ElementService import ElementService


class Element(BaseModel):
    name: str
    description: str
    category_id: int


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return index.getHtml()


@app.get("/api/v1/{name}/element")
def getElements(name: str):
    elementService = ElementService(name)
    return elementService.getElements()


@app.get("/api/v1/{name}/element/{id}")
def getElementById(name: str, id: int):
    elementService = ElementService(name)
    return elementService.getElement(id)


@app.post("/api/v1/{name}/element")
def postElement(name: str, element: Element):
    elementService = ElementService(name)
    return elementService.postElement(element)


@app.put("/api/v1/{name}/element/{id}")
def putElement(name: str, id: int, element: Element):
    elementService = ElementService(name)
    return elementService.putElement(id, element)
