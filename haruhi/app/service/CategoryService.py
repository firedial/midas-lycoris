from database.database import SessionLocal
from database.model import KindCategory


def getCategory():
    db = SessionLocal()

    kindCategory = KindCategory()
    kindCategory.name = "hoge"
    kindCategory.description = "hoge"

    try:
        db.add(kindCategory)
        db.commit()
    except Exception:
        print("error")

    users = db.query(KindCategory).all()
    return users[0]
