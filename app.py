from flask import Flask
from flask import Blueprint, render_template, redirect, url_for, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method=="POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with open('feedback.txt', 'a') as f:
            f.write(f'Name: {name}, Email: {email}, Message: {message}\n')
        return render_template('thankyou.html')
    else:
        return render_template("contact.html")

@app.route("/reviews")
def reviews():
    return render_template("reviews.html")

