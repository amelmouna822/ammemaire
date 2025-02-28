
from flask import Flask, render_template, request, redirect, url_for
from job_seekers import process_job_seeker
from companies import process_company

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")  # صفحة الترحيب

@app.route("/home")
def home():
    return render_template("home.html")  # الصفحة الرئيسية

@app.route("/job_seekers", methods=["GET", "POST"])
def job_seekers():
    return process_job_seeker(request)  # معالجة رفع السيرة الذاتية

@app.route("/companies", methods=["GET", "POST"])
def companies():
    return process_company(request)  # معالجة البحث عن السير الذاتية

if __name__ == "__main__":
    app.run()