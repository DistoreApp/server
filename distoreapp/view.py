from flask import Blueprint, abort, render_template

from distoreapp.utils import get_dump, get_message

bp = Blueprint("view", __name__)


@bp.route("/d/<string:code>")
def view_dump(code):
    dump = get_dump(code)

    if dump is None:
        abort(404)

    messages = [get_message(message_id) for message_id in dump.message_ids]

    return render_template("view.html", messages=messages)