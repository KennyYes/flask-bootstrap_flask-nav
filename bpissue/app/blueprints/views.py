from flask import render_template, redirect, url_for
from . import bp


@bp.route('/')
def home():
    # return render_template("home.html")
    return redirect(url_for("bp.fournotfive"))


@bp.route('/405')
def fournotfive():
    return render_template("405.html")
