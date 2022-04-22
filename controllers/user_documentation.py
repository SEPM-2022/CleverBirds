from flask import Flask, render_template, request, session, make_response
from app import app 

@app.route('/about', methods=["POST", "GET"])
def about():
    if request.method == "GET":
        return render_template('about.html')


@app.route('/privacy', methods=["POST", "GET"])
def privacy():
    if request.method == "GET":
        return render_template('privacy-policy.html')