from flask import current_app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(current_app.config["DATABASE"])

session_maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
session = scoped_session(sessionmaker)

Base = declarative_base()
Base.query = session.query_property()


def init_app():
    from . import models

    Base.metadata.create_all(bind=engine)
