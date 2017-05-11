from flask import Flask
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link
from flask_bootstrap import Bootstrap
topbar = Navbar(View("Home", "home"),
                Link("Source Code", r"http://www.github.com/d4d3vd4v3/tweet-analysis"))
nav = Nav()
nav.register_element("topbar", topbar)


def create_app():
    app = Flask(__name__)
    from .blueprints import bp
    app.register_blueprint(bp)
    Bootstrap(app)
    nav.init_app(app)
    return app
