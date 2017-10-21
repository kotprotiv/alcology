from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

import parsing_test

try:
    from local_settings import *
except ImportError:
    print('Не настроен локальный файл со строкой соединения с базой данных')
    raise

engine = create_engine(connection_string)

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

current = parsing_test.get_recipe('http://ru.inshaker.com/cocktails/903-uragan-punsh', 'recipe_text')
print(current)
