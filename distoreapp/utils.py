import random
import string

from distoreapp.models import Message, Dump


def random_dump_id():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(0, 10))


def get_dump(dump_id):
    return Dump.query.filter(Dump.dump_id == dump_id).first()


def get_message(message_id):
    return Message.query.filter(Message.message_id == message_id).first()