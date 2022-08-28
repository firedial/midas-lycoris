from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from static import index
from service.ElementService import ElementService, Element
from service.CategoryService import CategoryService, Category
from service.BalanceService import BalanceService, BalanceInput
from service.MoveService import MoveService, Move


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return index.getHtml()


# element
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


@app.delete("/api/v1/{name}/element/{id}")
def deleteElement(name: str, id: int):
    elementService = ElementService(name)
    return elementService.deleteElement(id)


# category
@app.get("/api/v1/{name}/category")
def getCategories(name: str):
    categoryService = CategoryService(name)
    return categoryService.getCategories()


@app.get("/api/v1/{name}/category/{id}")
def getCategoryById(name: str, id: int):
    categoryService = CategoryService(name)
    return categoryService.getCategory(id)


@app.post("/api/v1/{name}/category")
def postCategory(name: str, category: Category):
    categoryService = CategoryService(name)
    return categoryService.postCategory(category)


@app.put("/api/v1/{name}/category/{id}")
def putCategory(name: str, id: int, category: Category):
    categoryService = CategoryService(name)
    return categoryService.putCategory(id, category)


@app.delete("/api/v1/{name}/category/{id}")
def deleteCategory(name: str, id: int):
    categoryService = CategoryService(name)
    return categoryService.deleteCategory(id)


# balance
@app.get("/api/v1/balance")
def getBalances():
    balanceService = BalanceService()
    return balanceService.getBalances()


@app.get("/api/v1/balance/{id}")
def getBalanceById(id: int):
    balanceService = BalanceService()
    return balanceService.getBalanceById(id)


@app.post("/api/v1/balance")
def postBalance(balance: BalanceInput):
    balanceService = BalanceService()
    return balanceService.postBalance(balance)


@app.put("/api/v1/balance/{id}")
def putBalance(id: int, balance: BalanceInput):
    balanceService = BalanceService()
    return balanceService.putBalance(id, balance)


@app.delete("/api/v1/balance/{id}")
def deleteBalance(id: int):
    balanceService = BalanceService()
    return balanceService.deleteBalance(id)


# move
@app.get("/api/v1/{name}/move")
def getMoves(name: str):
    moveService = MoveService(name)
    return moveService.getMoves()


@app.get("/api/v1/{name}/move/{id}")
def getMoveById(name: str, id: int):
    moveService = MoveService(name)
    return moveService.getMoveById(id)


@app.post("/api/v1/{name}/move")
def postMove(name: str, move: Move):
    moveService = MoveService(name)
    return moveService.postMove(move)


@app.put("/api/v1/{name}/move/{id}")
def putMove(id: int, name: str, move: Move):
    moveService = MoveService(name)
    return moveService.putMove(id, move)


@app.delete("/api/v1/{name}/move/{id}")
def deleteMove(name: str, id: int):
    moveService = MoveService(name)
    return moveService.deleteMove(id)
