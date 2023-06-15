import logging

from sqlalchemy import func

from helixa_app.db.relational_db.models.category import Category
from helixa_app.db.relational_db.models.models_utils import get_children_ids
from helixa_app.db.relational_db.models.psychographic import Psychographic
from helixa_app.db.relational_db.session import context_session
from helixa_app.schema.file_schema import FileInfo
from helixa_app.schema.schema import RequestModel

log = logging.getLogger(__name__)


def populate_db_from_object(file_info_obj: 'FileInfo', configuration) -> None:
    with context_session(configuration) as session:
        for item in file_info_obj.values():
            session.add(file_info_obj.db_table(**item))
        try:
            session.commit()
        except Exception:
            log.exception("Error while committing objects for table %s", file_info_obj.db_table)


def _consume_query_result(query) -> list:
    return [record.as_dict() for record in query]


def get_from_request(session, _request: RequestModel):
    category_subquery = session.query(func.max(Category.level).label("level")).filter(
        Category.name.ilike(f"%{_request.value}%")).subquery()
    category_val = session.query(Category).filter(Category.name.ilike(f"%{_request.value}%"),
                                                  Category.level == category_subquery.c.level)
    psychographics_subquery = session.query(func.max(Psychographic.level).label("level")). \
        filter(Psychographic.label.ilike(f"%{_request.value}%")).subquery()
    psychographics_val = session.query(Psychographic). \
        filter(Psychographic.label.ilike(f"%{_request.value}%"),
               Psychographic.level == psychographics_subquery.c.level)

    # find recursively all the children and then query with id in list
    cat_children = session.query(Category.children).filter(Category.name == _request.sublayer).first()
    if cat_children:
        cat_sublayer_children_ids = get_children_ids(cat_children.children, children_key="children")
    else:
        cat_sublayer_children_ids = []
    cat_sublayer_val = session.query(func.max(Category.level).label("level")). \
        filter(Category.name.ilike(f"%{_request.value}%"),
               Category.id.in_(cat_sublayer_children_ids)).subquery()
    cat_sublayer_val = session.query(Category). \
        filter(Category.name.ilike(f"%{_request.value}%"),
               Category.id.in_(cat_sublayer_children_ids),
               Category.level == cat_sublayer_val.c.level)

    # find recursively all the values and then query with id in list
    psycho_values = session.query(Psychographic.values).filter(Psychographic.label == _request.sublayer).first()
    if psycho_values:
        psycho_sublayer_children_ids = get_children_ids(psycho_values.values, children_key="values")
    else:
        psycho_sublayer_children_ids = []
    psycho_sublayer_val = session.query(func.max(Psychographic.level).label("level")). \
        filter(Psychographic.label.ilike(f"%{_request.value}%"),
               Psychographic.id.in_(psycho_sublayer_children_ids)).subquery()
    psycho_sublayer_val = session.query(Psychographic). \
        filter(Psychographic.label.ilike(f"%{_request.value}%"),
               Psychographic.id.in_(psycho_sublayer_children_ids),
               Psychographic.level == psycho_sublayer_val.c.level)

    return {"category": _consume_query_result(category_val),
            "psychographics": _consume_query_result(psychographics_val),
            "category_sublayer": _consume_query_result(cat_sublayer_val),
            "psychographics_sublayer": _consume_query_result(psycho_sublayer_val)
            }
