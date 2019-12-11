from sqlalchemy import Column, String, BIGINT
from sqlalchemy.dialects import postgresql

from distoreapp.database import Base


class Dump(Base):
    __tablename__ = "dumps"

    dump_id = Column(String(10), primary_key=True, unique=True)
    message_ids = Column(postgresql.ARRAY(BIGINT))


class Message(Base):
    __tablename__ = "messages"

    message_id = Column(BIGINT, primary_key=True, unique=True)
    message_content = Column(String(2001))
    attachments = Column(postgresql.ARRAY(String))
    author_id = Column(BIGINT)
    author_name = Column(String(32))
    author_discriminator = Column(String(4))
    author_avatar_url = Column(String)
