import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from helixa_app.db.models.base import Base

log = logging.getLogger(__name__)


def create_db(connection_string: str) -> None:
    engine = create_engine(connection_string)
    Base.metadata.create_all(engine)


def create_session(connection_string: str) -> scoped_session:
    engine = create_engine(connection_string)
    return scoped_session(sessionmaker(bind=engine))


@contextmanager
def context_session(connection_string: str) -> None:
    log.debug("Creating session context")
    session = create_session(connection_string)
    log.debug("Session created")
    try:
        yield session
    except Exception as e:
        log.error("exception occurred while using session: %s", e)
        raise e
    finally:
        session.remove()
        log.debug("Session Closed")
