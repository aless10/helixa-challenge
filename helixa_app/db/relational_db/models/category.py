from sqlalchemy import Column, INTEGER, String

from helixa_app.db.relational_db.models.base import Base
from helixa_app.db.relational_db.models.models_utils import JsonBlob


class Category(Base):
    __tablename__ = 'categories'

    id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(String(64))
    level = Column(String(16))
    children = Column(JsonBlob(256), nullable=True)
    pic = Column(String(64))
    type = Column(String(64))
    l1 = Column(INTEGER, nullable=True)
    l2 = Column(INTEGER, nullable=True)
    l3 = Column(INTEGER, nullable=True)
    l4 = Column(INTEGER, nullable=True)
    l5 = Column(INTEGER, nullable=True)
