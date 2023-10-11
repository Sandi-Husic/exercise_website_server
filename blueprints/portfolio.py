from flask import Blueprint, render_template

portfolio_bp = Blueprint("portfolio", __name__)


@portfolio_bp.route("/portfolio", methods=["GET"])
def portfolio():
    return render_template("portfolio.html")
