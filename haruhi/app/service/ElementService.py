from database.database import SessionLocal
from database.model import KindElement, PurposeElement, PlaceElement


class ElementService:
    def __init__(self, elementName: str):
        match elementName:
            case "kind":
                self.element = KindElement
            case "purpose":
                self.element = PurposeElement
            case "place":
                self.element = PlaceElement
            case _:
                raise Exception("not support element name: " + elementName)

    def getElements(self):
        db = SessionLocal()
        return db.query(self.element).all()
