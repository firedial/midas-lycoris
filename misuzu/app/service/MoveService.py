from pydantic import BaseModel

from database.database import SessionLocal
from database.model import Balance
from service.ElementService import KIND_ELEMENT_MOVE_ID, PURPOSE_ELEMENT_MOVE_ID, PLACE_ELEMENT_MOVE_ID


class Move(BaseModel):
    amount: int
    item: str
    before_id: int
    after_id: int
    date: str


class MoveService:
    def __init__(self, elementName: str):
        self.db = SessionLocal()
        match elementName:
            case "purpose":
                self.move = "purpose"
            case "place":
                self.move = "place"
            case _:
                raise Exception("not support move element name: " + elementName)

    def __del__(self):
        self.db.close()

    def getMoves(self):
        balances = self.db.query(Balance).filter(Balance.kind_element_id == KIND_ELEMENT_MOVE_ID, Balance.amount < 0)
        return list(map(self.balanceToMove, balances))

    def getMoveById(self, id: int):
        balanceBefore = self.db.query(Balance).filter(Balance.id == id, Balance.kind_element_id == KIND_ELEMENT_MOVE_ID, Balance.amount < 0).one()

        return self.balanceToMove(balanceBefore)

    def postMove(self, move: Move):
        balanceBefore = Balance()
        balanceBefore.amount = (-1) * move.amount
        balanceBefore.item = move.item
        balanceBefore.date = move.date
        balanceBefore.kind_element_id = KIND_ELEMENT_MOVE_ID

        balanceAfter = Balance()
        balanceAfter.amount = move.amount
        balanceAfter.item = move.item
        balanceAfter.date = move.date
        balanceAfter.kind_element_id = KIND_ELEMENT_MOVE_ID

        if self.move == "purpose":
            balanceBefore.purpose_element_id = move.before_id
            balanceBefore.place_element_id = PLACE_ELEMENT_MOVE_ID

            balanceAfter.purpose_element_id = move.after_id
            balanceAfter.place_element_id = PLACE_ELEMENT_MOVE_ID

        elif self.move == "place":
            balanceBefore.purpose_element_id = PURPOSE_ELEMENT_MOVE_ID
            balanceBefore.place_element_id = move.before_id

            balanceAfter.purpose_element_id = PURPOSE_ELEMENT_MOVE_ID
            balanceAfter.place_element_id = move.after_id

        self.db.add(balanceBefore)
        self.db.add(balanceAfter)
        self.db.commit()

    def putMove(self, id: int, move):
        balanceBefore = self.db.query(Balance).filter(Balance.id == id, Balance.kind_element_id == KIND_ELEMENT_MOVE_ID, Balance.amount < 0).one()
        balanceAfter = self.db.query(Balance).filter(Balance.id == id + 1, Balance.kind_element_id == KIND_ELEMENT_MOVE_ID, Balance.amount > 0).one()

        balanceBefore.amount = (-1) * move.amount
        balanceBefore.item = move.item
        balanceBefore.date = move.date
        balanceBefore.kind_element_id = KIND_ELEMENT_MOVE_ID

        balanceAfter.amount = move.amount
        balanceAfter.item = move.item
        balanceAfter.date = move.date
        balanceAfter.kind_element_id = KIND_ELEMENT_MOVE_ID

        if self.move == "purpose":
            balanceBefore.purpose_element_id = move.before_id
            balanceBefore.place_element_id = PLACE_ELEMENT_MOVE_ID

            balanceAfter.purpose_element_id = move.after_id
            balanceAfter.place_element_id = PLACE_ELEMENT_MOVE_ID

        elif self.move == "place":
            balanceBefore.purpose_element_id = PURPOSE_ELEMENT_MOVE_ID
            balanceBefore.place_element_id = move.before_id

            balanceAfter.purpose_element_id = PURPOSE_ELEMENT_MOVE_ID
            balanceAfter.place_element_id = move.after_id

        self.db.commit()

    def deleteMove(self, id: int):
        self.db.query(Balance).filter(Balance.id == id, Balance.kind_element_id == KIND_ELEMENT_MOVE_ID, Balance.amount < 0).delete()
        self.db.query(Balance).filter(Balance.id == id + 1, Balance.kind_element_id == KIND_ELEMENT_MOVE_ID, Balance.amount > 0).delete()
        self.db.commit()

    def balanceToMove(self, before: Balance) -> Move:
        return Move(
            before_id=before.id,
            after_id=before.id + 1,
            item=before.item,
            amount=(-1) * before.amount,
            date=str(before.date),
        )
