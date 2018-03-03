from database import db_session


def query(_type):
    return db_session.query(_type)

def add_entry(datetime, string):
    t = TbTest(datetime, string)
    db_session.add(t)
    db_session.commit()


def delete_entry(datetime, string):
    db_session.query(TbTest).filter(TbTest.datetime == datetime, TbTest.string == string).delete()
    db_session.commit()


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
