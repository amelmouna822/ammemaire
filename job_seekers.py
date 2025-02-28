from flask import render_template, request, redirect, url_for
from utils import process_resume
from database import insert_resume

def process_job_seeker(request):
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        uploaded_file = request.files["resume"]
        
        if uploaded_file and name and email:
            resume_text = process_resume(uploaded_file)
            insert_resume(name, email, resume_text)
            return render_template("job_seekers.html", success=True)

    return render_template("job_seekers.html", success=False)
