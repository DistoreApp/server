from flask import Blueprint, request

bp = Blueprint("api", __name__)


@bp.route("/store", methods=["POST"])
def store():
    data = request.get_json()
