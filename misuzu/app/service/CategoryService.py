from pydantic import BaseModel

from database.database import SessionLocal
from database.model import KindCategory, PurposeCategory, PlaceCategory


class Category(BaseModel):
    name: str
    description: str


class CategoryService:
    def __init__(self, categoryName: str):
        self.db = SessionLocal()
        match categoryName:
            case "kind":
                self.Category = KindCategory
            case "purpose":
                self.Category = PurposeCategory
            case "place":
                self.Category = PlaceCategory
            case _:
                raise Exception("not support category name: " + categoryName)

    def __del__(self):
        self.db.close()

    def getCategories(self):
        return self.db.query(self.Category).all()

    def getCategory(self, id: int):
        return self.db.query(self.Category).filter(self.Category.id == id).one()

    def postCategory(self, categoryValue: Category):
        Category = self.Category()
        Category.name = categoryValue.name
        Category.description = categoryValue.description

        self.db.add(Category)
        self.db.commit()

    def putCategory(self, id: int, categoryValue: Category):
        Category = self.db.query(self.Category).filter(self.Category.id == id).one()
        Category.name = categoryValue.name
        Category.description = categoryValue.description

        self.db.commit()

    def deleteCategory(self, id: int):
        self.db.query(self.Category).filter(self.Category.id == id).delete()
        self.db.commit()
