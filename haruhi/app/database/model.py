from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.database import Base, engine


class KindCategory(Base):
    __tablename__ = "m_kind_category"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(20), index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    element = relationship("KindElement", uselist=True)


class KindElement(Base):
    __tablename__ = "m_kind_element"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(20), index=True, nullable=False)
    catecory_id = Column(Integer, ForeignKey("m_kind_category.id"), index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    category = relationship("KindCategory", uselist=False)


Base.metadata.create_all(bind=engine)
