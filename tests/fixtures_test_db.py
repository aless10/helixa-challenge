import pytest
from sqlalchemy.orm import sessionmaker

from helixa_app.db.relational_db.session import create_db
from helixa_app.db.relational_db.models.category import Category
from helixa_app.db.relational_db.models.psychographic import Psychographic


def db_session():
    engine = create_db('sqlite://')
    session = sessionmaker(bind=engine)()
    return session


@pytest.fixture(scope='function')
def local_session(category_objects, psychographics_objects):
    session = db_session()
    session.add_all(category_objects)
    session.add_all(psychographics_objects)
    session.commit()
    return session


@pytest.fixture
def category_objects():
    category_1 = Category(
        id=1,
        name="test_parent_1",
        level=1,
        children=[{"id": 2, "name": "test_children_1", "level": 2},
                  {"id": 3, "name": "test_children_2", "level": 2}],
    )
    category_2 = Category(
        id=2,
        name="test_children_1",
        level=2,
        children=[]
    )

    category_3 = Category(
        id=3,
        name="test_children_2",
        level=2,
        children=[]
    )

    return [category_1, category_2, category_3]


@pytest.fixture
def psychographics_objects():
    psycho_1 = Psychographic(
        id="1",
        label="1",
        level="1",
        value="1",
        values="1",
        sources="1",
        pic="1",
        ico="1",
        addonId="1",
    )

    return [psycho_1]
