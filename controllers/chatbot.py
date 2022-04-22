from flask import Flask, render_template, request, session, make_response
from app import app 


@app.route('/tweety', methods=["POST", "GET"])
def talk():
    if request.method == "GET":
        return render_template('tweety.html')