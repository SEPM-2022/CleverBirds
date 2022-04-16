import os

from flask import Flask, render_template, request, session, redirect, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# database = 'CleverBirds_MYDB'
# username = 'sa'
# password = '#SenhadoSA123'

# connection string
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '6w33tOXubzT64MocVvg9Kg'

db = SQLAlchemy(app)
from models import *



@app.route('/signup', methods=["POST", "GET"])
def page_signup():
    if request.method == "POST":
        form = request.form.to_dict()

        # Generating password hash
        password_hash = generate_password_hash(form.get('password'))

        # Create new user
        new_user = CleverUsers(U_Name=form.get('name'),
                               U_Username=form.get('username'),
                               U_Password=password_hash,
                               U_Email=form.get('email'),
                               U_Score=form.get('score'),
                               U_CharacterName=form.get('avatar'),
                               U_Gender=form.get('gender'))

        db.session.add(new_user)
        db.session.commit()

        return render_template('signup-success.html')

    elif request.method == "GET":
        return render_template('create-account.html')


@app.route('/', methods=["POST", "GET"])
@app.route('/login', methods=["POST", "GET"])
def page_login():
    if request.method == "POST":
        form = request.form.to_dict()

        user = CleverUsers.query.filter_by(U_Username=form.get('username')).first()

        if user is None:
            print("User not found")
            flash("This user does not exist! Please create your account :)")
        else:
            if check_password_hash(user.U_Password, form.get('password')):
                session['logged_user'] = user.U_Id

                return render_template('user-dashboard.html', Name=user.U_Name, Username=user.U_Username,
                                       Avatar=user.U_CharacterName, Score=user.U_Score)
            else:
                flash("Wrong username/password.")

    return render_template('index.html')


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


@app.route('/about', methods=["POST", "GET"])
def about():
    if request.method == "GET":
        return render_template('about.html')


@app.route('/privacy', methods=["POST", "GET"])
def privacy():
    if request.method == "GET":
        return render_template('privacy-policy.html')


@app.route('/changeavatar', methods=["POST", "GET"])
def change_avatar():
    if request.method == "GET":
        return render_template('change-avatar.html')


@app.route('/useraccount', methods=["POST", "GET"])
def manage_account():
    if request.method == "GET":

        user_id = session.get('logged_user')
        user = CleverUsers.query.filter_by(U_Id=user_id).first()

        if user is None:
            return redirect('/')

        return render_template('manage-account.html', Id=user.U_Id, Name=user.U_Name, Username=user.U_Username,
                               Email=user.U_Email, Score=user.U_Score)

    else:
        if request.method == "POST":
            user_to_delete = session['logged_user']
            user_found_to_delete = CleverUsers.query.filter_by(U_Id=user_to_delete).first()
            db.session.delete(user_found_to_delete)
            db.session.commit()
            flash("Your account has been successfully deleted. We are sorry to see you go.")
            return redirect('/')


@app.route('/save-score/<score>', methods=["GET"])
def save_score(score):
    user_id = session['logged_user']
    user = CleverUsers.query.filter_by(U_Id=user_id).first()
    user.U_Score = score
    db.session.add(user)
    db.session.commit()
    return make_response("OK", 200)


@app.route('/tweety', methods=["POST", "GET"])
def talk():
    if request.method == "GET":
        return render_template('tweety.html')


if __name__ == "__main__":
    # create scrip only once

    app.run(debug=True)
