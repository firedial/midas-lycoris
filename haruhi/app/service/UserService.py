from database.database import SessionLocal
from database.model import User


def getUser():
    db = SessionLocal()

    user = User()
    user.email = "fuga"
    user.hashed_password = "hoge"
    user.is_active = True

    try:
        db.add(user)
        db.commit()
    except Exception:
        print("error")

    users = db.query(User).all()
    return users[0]
