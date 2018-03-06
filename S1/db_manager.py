from database import Session

scoped_session = None
def query(_type):
    if scoped_session is None:
        return None
    return scoped_session.query(_type)


def update_entry():
    if scoped_session is None:
        return
    scoped_session.flush()


# def db_delete():
#     o = db_session.query(TbTest).filter(TbTest.id == 3).first()
#     if o is None:
#         return 'none'
#
#     db_session.delete(o)
#     return 'delete succes'


def db_commit():
    if scoped_session is None:
        return
    scoped_session.commit()


def db_flush():
    if scoped_session is None:
        return
    scoped_session.flush()


def main():
    if scoped_session is None:
        return
    scoped_session.close()


def after_request():
    print 'after_request'
    global scoped_session
    if scoped_session is not None:
        scoped_session.close()


def before_request():
    print 'before_request'
    global scoped_session
    scoped_session = Session()


