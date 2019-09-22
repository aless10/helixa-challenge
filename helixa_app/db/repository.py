from helixa_app.db.session import context_session
from helixa_app.schema.file_schema import FileInfo


def populate_db_from_object(file_info_obj: 'FileInfo', configuration) -> None:
    with context_session(configuration) as session:
        for item in file_info_obj.values():
            session.add(file_info_obj.db_table(**item))
            try:
                session.commit()
            except Exception as e:
                print(e)
