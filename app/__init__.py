"""
MAIN APP ROUTES
"""

from flask import Flask
from flask import render_template


app = Flask(__name__)


# -------------------------------------------------------
@app.get("/")
def hello():
    """
    Home Page
    """
    return render_template("pages/home.jinja")


# -------------------------------------------------------
@app.get("/about")
def about():
    """
    About page
    """
    return render_template("pages/about.jinja")
