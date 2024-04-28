from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/gohome")
def go_home():
    return redirect(url_for("views.home"))

@views.route("/about")
def about():
    return render_template("about.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/reviews")
def reviews():
    return render_template("reviews.html")