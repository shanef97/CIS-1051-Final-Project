from flask import Blueprint, render_template, redirect, url_for, request
from app import app
from flask_mail import Mail, Message

views = Blueprint(__name__, "views")

mail = Mail(app)

app.config.update(dict(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'ferrellshane470@gmail.com',
    MAIL_PASSWORD = "b8wja'tQ13.0"
))

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
        msg = Message('Test', sender='mymail@mail.com', recipients=['mymai@mail.com'])
        msg.body = "Contact form submitted with data:\n\nName: {}\n\nE-mail: {}\n\nMessage: {}".format(name, email, message)
        mail.send(msg)

        return render_template('thankyou.html')
    else:
        return render_template("contact.html")