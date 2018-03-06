from database import db_session

scoped_session = None
def query(_type):
    if db_session is None:
        return None
    return db_session.query(_type)


def update_entry():
    if db_session is None:
        return
    db_session.flush()


# def db_delete():
#     o = db_session.query(TbTest).filter(TbTest.id == 3).first()
#     if o is None:
#         return 'none'
#
#     db_session.delete(o)
#     return 'delete succes'


def db_commit():
    if db_session is None:
        return
    db_session.commit()


def db_flush():
    if db_session is None:
        return
    db_session.flush()


def session_close():
    if db_session is None:
        return
    db_session.close()


def after_request():
    db_session.flush()


def before_request():
    db_session.flush()


