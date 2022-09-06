from pydantic import BaseModel

from database.database import SessionLocal
from database.model import Balance
from service.ElementService import KIND_ELEMENT_MOVE_ID


class BalanceInput(BaseModel):
    amount: int
    item: str
    kind_element_id: int
    purpose_element_id: int
    place_element_id: int
    date: str


class BalanceService:
    def __init__(self):
        self.db = SessionLocal()

    def __del__(self):
        self.db.close()

    def getBalances(self):
        return self.db.query(Balance).filter(Balance.kind_element_id != KIND_ELEMENT_MOVE_ID).all()

    def getBalanceById(self, id: int):
        return self.db.query(Balance).filter(Balance.id == id, Balance.kind_element_id == KIND_ELEMENT_MOVE_ID).one()

    def postBalance(self, balanceValue: BalanceInput):
        balance = Balance()
        balance.amount = balanceValue.amount
        balance.item = balanceValue.item
        balance.kind_element_id = balanceValue.kind_element_id
        balance.purpose_element_id = balanceValue.purpose_element_id
        balance.place_element_id = balanceValue.place_element_id
        balance.date = balanceValue.date

        self.db.add(balance)
        self.db.commit()

    def putBalance(self, id: int, balanceValue: BalanceInput):
        balance = self.db.query(Balance).filter(Balance.id == id, Balance.kind_element_id != KIND_ELEMENT_MOVE_ID).one()
        balance.amount = balanceValue.amount
        balance.item = balanceValue.item
        balance.kind_element_id = balanceValue.kind_element_id
        balance.purpose_element_id = balanceValue.purpose_element_id
        balance.place_element_id = balanceValue.place_element_id
        balance.date = balanceValue.date

        self.db.commit()

    def deleteBalance(self, id: int):
        self.db.query(Balance).filter(Balance.id == id, Balance.kind_element_id != KIND_ELEMENT_MOVE_ID).delete()
        self.db.commit()
