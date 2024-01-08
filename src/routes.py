from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/sender")
def sender():
    return render_template("sender.html")

@main.route("/receiver")
def receiver():
    return render_template("receiver.html")