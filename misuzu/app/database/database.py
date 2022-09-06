from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "mysql://{user}:{password}@{host}/{db}?charset=utf8".format(
    host=os.environ["MYSQL_HOST"],
    db=os.environ["MYSQL_DATABASE"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Setting(object):
    __table_args__ = {
        "mysql_default_charset": "utf8mb4",
        "mysql_collate": "utf8mb4_bin",
        "mysql_engine": "InnoDB",
        "mysql_row_format": "DYNAMIC",
    }


Base = declarative_base(cls=Setting)
