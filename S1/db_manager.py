from database import db_session


def query(_type):
    return db_session.query(_type)


def update_entry():
    db_session.flush()


# def db_delete():
#     o = db_session.query(TbTest).filter(TbTest.id == 3).first()
#     if o is None:
#         return 'none'
#
#     db_session.delete(o)
#     return 'delete succes'


def db_commit():
    db_session.commit()


def db_flush():
    db_session.flush()


def main():
    db_session.close()
