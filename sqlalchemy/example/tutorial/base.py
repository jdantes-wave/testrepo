# https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_NAME = 'bravo_db'
DB_PORT = 5432
DB_USER = 'bravo_user'
DB_PASSWORD = 'bravo_password'

engine = create_engine('postgresql://%s:%s@localhost:%d/%s' % (DB_USER, DB_PASSWORD, DB_PORT, DB_NAME))
Session = sessionmaker(bind=engine)

Base = declarative_base()
