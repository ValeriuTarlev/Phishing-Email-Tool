from flask import Blueprint, render_template, request
from phishing_rules import analyze_email

main = Blueprint('main', __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        subject = request.form.get("subject", "")
        body = request.form.get("body", "")
        sender = request.form.get("sender", "")
        link = request.form.get("link", "")

        print("Subject:", subject)
        print("Body:", body)
        print("Sender:", sender)
        print("Link:", link)

        if body and sender:
            result = analyze_email(subject, body, sender, link)

    return render_template("index.html", result=result) 
