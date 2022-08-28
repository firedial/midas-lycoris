from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from static import index

from service.ElementService import ElementService

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return index.getHtml()


@app.get("/api/v1/{name}/element")
def read_item(name: str):
    elementService = ElementService(name)
    return elementService.getElements()
