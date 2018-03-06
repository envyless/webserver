# database.py
#!/usr/bin/python

#########################################
#     python 2.7.3
#########################################

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:@localhost/testdb', convert_unicode=False)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = Session()

Base = declarative_base()


def init_db():
  Base.metadata.create_all(engine)
