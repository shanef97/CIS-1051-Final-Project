from flask import Blueprint, render_template, redirect, url_for, request

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/about")
def about():
    return render_template("about.html")


@views.route("/reviews")
def reviews():
    return render_template("reviews.html")