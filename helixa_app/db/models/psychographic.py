from sqlalchemy import Column, String

from helixa_app.db.models.base import Base
from helixa_app.db.models.models_utils import JsonBlob


class Psychographic(Base):
    __tablename__ = 'psychographics'

    id = Column(String(64), primary_key=True, nullable=False)
    label = Column(String(64), nullable=False)
    level = Column(String(16))
    value = Column(String(64))
    values = Column(JsonBlob(256))
    sources = Column(JsonBlob(256))
    pic = Column(String(64))
    ico = Column(String(16))
    addonId = Column(String(16))
