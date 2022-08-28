from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
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
    category_id = Column(Integer, ForeignKey("m_kind_category.id"), index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    category = relationship("KindCategory", uselist=False)
    balance = relationship("Balance", uselist=True)


class PurposeCategory(Base):
    __tablename__ = "m_purpose_category"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(20), index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    element = relationship("PurposeElement", uselist=True)


class PurposeElement(Base):
    __tablename__ = "m_purpose_element"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(20), index=True, nullable=False)
    category_id = Column(Integer, ForeignKey("m_purpose_category.id"), index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    category = relationship("PurposeCategory", uselist=False)
    balance = relationship("Balance", uselist=True)


class PlaceCategory(Base):
    __tablename__ = "m_place_category"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(20), index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    element = relationship("PlaceElement", uselist=True)


class PlaceElement(Base):
    __tablename__ = "m_place_element"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(20), unique=True, index=True, nullable=False)
    description = Column(String(20), index=True, nullable=False)
    category_id = Column(Integer, ForeignKey("m_place_category.id"), index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    category = relationship("PlaceCategory", uselist=False)
    balance = relationship("Balance", uselist=True)


class Balance(Base):
    __tablename__ = "m_balance"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Integer, index=True, nullable=False)
    item = Column(String(50), nullable=False)
    kind_element_id = Column(Integer, ForeignKey("m_kind_element.id"), index=True, nullable=False)
    purpose_element_id = Column(Integer, ForeignKey("m_purpose_element.id"), index=True, nullable=False)
    place_element_id = Column(Integer, ForeignKey("m_place_element.id"), index=True, nullable=False)
    date = Column(Date, index=True, nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    kind = relationship("KindElement", uselist=False)
    purpose = relationship("PurposeElement", uselist=False)
    place = relationship("PlaceElement", uselist=False)


Base.metadata.create_all(bind=engine)
