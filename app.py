
from flask import Flask, render_template, request, redirect, url_for
from job_seekers import process_job_seeker
from companies import process_company

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")  # صفحة الترحيب
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/Jobs")
def Jobs():
    return render_template("Jobs.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/home")
def home():
    return render_template("home.html")  # الصفحة الرئيسية
@app.route("/login_job_seeker")
def login_job_seeker():
    return render_template("login_job_seeker.html")


@app.route("/login_company")
def login_company():
    return render_template("login_company.html")


@app.route("/job_seekers", methods=["GET", "POST"])
def job_seekers():
    return process_job_seeker(request)  # معالجة رفع السيرة الذاتية

@app.route("/companies", methods=["GET", "POST"])
def companies():
    return process_company(request)  # معالجة البحث عن السير الذاتية

if __name__ == "__main__":
    app.run()