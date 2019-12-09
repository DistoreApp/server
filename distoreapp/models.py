from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from distoreapp.database import Base


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    discriminator = Column(String(4))
    avatar_url = Column(String(128))

    messages = relationship("Message", backref="author", lazy=True)

    def __repr__(self):
        return "<Author {}>".format(self.id)


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    content = Column(String(2000))

    author_id = Column(Integer, ForeignKey("author.id"))

    attachments = relationship("Attachment", backref="message", lazy=True)


class Attachment(Base):
    __tablename__ = "attachments"

    id = Column(Integer, primary_key=True)
    url = Column(String(1028))

    message_id = Column(Integer, ForeignKey("message.id"))

