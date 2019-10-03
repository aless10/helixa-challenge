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


def get_from_request(db, _request: RequestModel):
    category_val = db.categories.find({"name": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"}},
                                      {"_id": 0})
    psychographics_val = db.psychographics.find({"label": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"}},
                                                {"_id": 0})
    cat_sublayer_val = db.categories.find({"children.name": {"$regex": f".*{_request.value.lower()}.*",
                                                             "$options": "i"},
                                           "name": _request.sublayer},
                                          {"_id": 0})
    psycho_sublayer_val = db.psychographics.find(
        {"values.label": {"$regex": f".*{_request.value.lower()}.*", "$options": "i"},
         "label": _request.sublayer},
        {"_id": 0})
    return {"category": [x for x in category_val],
            "psychographics": [x for x in psychographics_val],
            "category_sublayer": [x for x in cat_sublayer_val],
            "psychographics_sublayer": [x for x in psycho_sublayer_val]
            }
