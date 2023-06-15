# flake8: noqa
# pylint: skip-file
from sqlalchemy.ext.declarative import declarative_base


class DeclarativeBase:
    __table__ = None

    def as_dict(self):
        return {col: getattr(self, col) for col in self.__table__.columns.keys()}


Base = declarative_base(cls=DeclarativeBase)
