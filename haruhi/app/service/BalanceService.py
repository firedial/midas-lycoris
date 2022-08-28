from database.database import SessionLocal
from database.model import Balance


class BalanceService:
    def __init__(self):
        self.db = SessionLocal()

    def __del__(self):
        self.db.close()

    def getBalances(self):
        return self.db.query(Balance).all()

    def getBalanceById(self, id: int):
        return self.db.query(Balance).filter(Balance.id == id).one()

    def postBalance(self, balanceValue):
        balance = Balance()
        balance.amount = balanceValue.amount
        balance.item = balanceValue.item
        balance.kind_element_id = balanceValue.kind_element_id
        balance.purpose_element_id = balanceValue.purpose_element_id
        balance.place_element_id = balanceValue.place_element_id
        balance.date = balanceValue.date

        self.db.add(balance)
        self.db.commit()

    def putBalance(self, id: int, balanceValue):
        balance = self.db.query(Balance).filter(Balance.id == id).first()
        balance.amount = balanceValue.amount
        balance.item = balanceValue.item
        balance.kind_element_id = balanceValue.kind_element_id
        balance.purpose_element_id = balanceValue.purpose_element_id
        balance.place_element_id = balanceValue.place_element_id
        balance.date = balanceValue.date

        self.db.commit()

    def deleteBalance(self, id: int):
        self.db.query(Balance).filter(Balance.id == id).delete()
        self.db.commit()
