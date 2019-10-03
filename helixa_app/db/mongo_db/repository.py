import logging
import os

from helixa_app.db.mongo_db.session import context_db
from helixa_app.schema.file_schema import FileInfo
from helixa_app.schema.schema import RequestModel

log = logging.getLogger(__name__)


def populate_mongo_db_from_object(file_info_obj: FileInfo, configuration: str):
    collection_name = os.path.basename(file_info_obj.filename).split(".")[0]
    with context_db(configuration) as db:
        coll = getattr(db, str(collection_name))
        if coll.count() == 0:
            log.info("initialize collection %s", collection_name)
            for element in file_info_obj.info.values():
                coll.insert_one(element)
        else:
            log.info("collection %s already populated. Skipping", collection_name)


def _get_level(cursor):
    try:
        return cursor[0].get("level", 1)
    except IndexError:
        return 1


def get_from_request(db, _request: RequestModel):
    cat_level = _get_level(db.categories.find({"name": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"}},
                                              {"_id": 0, "level": 1}).sort([("level", -1)]).limit(1))
    category_val = db.categories.find(
        {"name": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"}, "level": cat_level},
        {"_id": 0})
    psychographics_level = _get_level(db.psychographics.find(
        {"label": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"}},
        {"_id": 0, "level": 1}).sort([("level", -1)]).limit(1))
    psychographics_val = db.psychographics.find({"label": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"},
                                                 "level": psychographics_level},
                                                {"_id": 0})
    cat_sublayer_val = db.categories.find({"children.name": {"$regex": f".*{_request.value.lower()}.*",
                                                             "$options": "i"},
                                           "children.level": cat_level,
                                           "name": _request.sublayer},
                                          {"_id": 0})
    psycho_sublayer_val = db.psychographics.find(
        {"values.label": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"},
         "values.level": psychographics_level,
         "label": _request.sublayer},
        {"_id": 0})
    return {"category": [x for x in category_val],
            "psychographics": [x for x in psychographics_val],
            "category_sublayer": [x for x in cat_sublayer_val],
            "psychographics_sublayer": [x for x in psycho_sublayer_val]
            }
