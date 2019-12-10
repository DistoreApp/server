from flask import Blueprint, request
from sqlalchemy.exc import IntegrityError

from distoreapp.models import Message, Dump
from distoreapp.database import session
from distoreapp.utils import random_dump_id, get_message

bp = Blueprint("api", __name__)


@bp.route("/store", methods=["POST"])
def store():
    data = request.get_json()

    messages = data.get("messages")
    message_ids = []

    for message in messages:
        message_ids.append(message.get("message_id"))

        if get_message(message.get("message_id")) is None:
            message = Message(
                message_id=message.get("message_id"),
                message_content=message.get("message_content"),
                attachments=message.get("attachments"),
                author_id=message.get("author_id"),
                author_name=message.get("author_name"),
                author_discriminator=message.get("author_discriminator"),
                author_avatar_url=message.get("author_avatar_url")
            )

            session.add(message)

    session.commit()

    while True:
        try:
            dump = Dump(
                dump_id=random_dump_id(),
                message_ids=message_ids
            )

            session.add(dump)
            session.commit()
        except IntegrityError:
            continue
        break

    return {"code": dump.dump_id}

