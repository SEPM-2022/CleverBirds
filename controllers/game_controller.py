
from flask import Flask, render_template, request, session, make_response
from app import app 
from models.clever_users import *

@app.route('/playgame', methods=["POST", "GET"])
def playing_game():
    if request.method == "GET":
        user_id = session.get('logged_user')
        user = CleverUsers.query.filter_by(U_Id=user_id).first()
        if user is None or user.U_CharacterName is None:
            bird = "def"
        else:
            bird = user.U_CharacterName

        return render_template('playgame.html', bird_png=bird)


@app.route('/save-score/<score>', methods=["GET"])
def save_score(score):
    user_id = session['logged_user']
    user = CleverUsers.query.filter_by(U_Id=user_id).first()
    user.U_Score = score
    #db.session.add(user) # needs to be deleted because add would add a new user and in the previous line the update was done already: https://stackoverflow.com/questions/6699360/flask-sqlalchemy-update-a-rows-information
    db.session.commit()
    return make_response("OK", 200)


