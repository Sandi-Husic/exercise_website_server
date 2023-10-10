from flask import Blueprint, render_template

resume_bp = Blueprint("resume", __name__)


@resume_bp.route("/resume", methods=["GET"])
def resume():
    return render_template("portfolio.html")
