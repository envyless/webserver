from database import Session


def query(_type):
    return Session().query(_type)


def update_entry():
    Session().flush()


# def db_delete():
#     o = db_session.query(TbTest).filter(TbTest.id == 3).first()
#     if o is None:
#         return 'none'
#
#     db_session.delete(o)
#     return 'delete succes'


def db_commit():
    Session().commit()


def db_flush():
    Session().flush()


def main():
    Session().close()
