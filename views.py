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

@views.route("/foodtrucks")
def foodtrucks():
    return render_template("foodtrucks.html")


@views.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        name = request.form.get['name']
        email = request.form.get['email']
        message = request.form.get['message']

        return render_template('thankyou.html')
    else:
        return render_template("contact.html")