from pydantic import BaseModel

from database.database import SessionLocal
from database.model import KindElement, PurposeElement, PlaceElement

KIND_ELEMENT_MOVE_ID = 1
PURPOSE_ELEMENT_MOVE_ID = 1
PLACE_ELEMENT_MOVE_ID = 1


class Element(BaseModel):
    name: str
    description: str
    category_id: int


class ElementService:
    def __init__(self, elementName: str):
        self.db = SessionLocal()
        match elementName:
            case "kind":
                self.Element = KindElement
            case "purpose":
                self.Element = PurposeElement
            case "place":
                self.Element = PlaceElement
            case _:
                raise Exception("not support element name: " + elementName)

    def __del__(self):
        self.db.close()

    def getElements(self):
        return self.db.query(self.Element).all()

    def getElement(self, id: int):
        return self.db.query(self.Element).filter(self.Element.id == id).one()

    def postElement(self, elementValue: Element):
        element = self.Element()
        element.name = elementValue.name
        element.description = elementValue.description
        element.category_id = elementValue.category_id

        self.db.add(element)
        self.db.commit()

    def putElement(self, id: int, elementValue: Element):
        element = self.db.query(self.Element).filter(self.Element.id == id).one()
        element.name = elementValue.name
        element.description = elementValue.description
        element.category_id = elementValue.category_id

        self.db.commit()

    def deleteElement(self, id: int):
        self.db.query(self.Element).filter(self.Element.id == id).delete()
        self.db.commit()
