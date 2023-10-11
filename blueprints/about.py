from flask import Blueprint, render_template
from blueprints.data.about_entry import about_entries

about_bp = Blueprint("about", __name__)


@about_bp.route("/about", methods=["GET"])
def about():
    active_entry = None
    for entry in about_entries:
        if entry["isActive"]:
            active_entry = entry
            break
    return render_template("about.html", active_entry=active_entry)
