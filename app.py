import os

from flask import Flask, render_template, request, session, redirect, flash
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


class CleverUsers(db.Model):
    U_Id = db.Column(db.Integer, primary_key=True)
    U_Name = db.Column(db.String(40), unique=False, nullable=False)
    U_Username = db.Column(db.String(20), unique=False, nullable=False)
    U_Password = db.Column(db.String(120), unique=False, nullable=False)
    U_Email = db.Column(db.String(80), unique=False, nullable=False)
    U_Score = db.Column(db.String(20), unique=False, nullable=True)
    U_CharacterName = db.Column(db.String(20), unique=False, nullable=False)
    U_Gender = db.Column(db.String(20), unique=False, nullable=False)

    def __repr__(self):
        return '<UserID %r>' % self.U_Id


class GameInstance(db.Model):
    GaI_Id = db.Column(db.Integer, primary_key=True)
    GaI_User_Id = db.Column(db.String(80), unique=False, nullable=False)
    GaI_date = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<UserID %r>' % self.GaI_User_Id


class Music(db.Model):
    Mus_Id = db.Column(db.Integer, primary_key=True)
    Mus_Name = db.Column(db.String(80), unique=False, nullable=False)
    Mus_Lenght = db.Column(db.String(80), unique=False, nullable=False)
    Mus_Artist = db.Column(db.String(80), unique=False, nullable=False)
    Mus_Licence = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<MusicId %r>' % self.Mus_Id


db.create_all()


# name, username, password, email, avatar, gender

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
                session['logged_user'] = {'Name': user.U_Name,
                                          'Username': user.U_Name,
                                          'Avatar': user.U_CharacterName,
                                          'Score': user.U_Score,
                                          'Email': user.U_Email,
                                          'Id': user.U_Id
                                          }

                return render_template('user-dashboard.html', Name=user.U_Name, Username=user.U_Username,
                                       Avatar=user.U_CharacterName, Score=user.U_Score)
            else:
                flash("Wrong username/password.")

    return render_template('index.html')


@app.route('/playgame', methods=["POST", "GET"])
def playing_game():
    if request.method == "GET":
        return render_template('playgame.html')


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
        user = session.get('logged_user')
        if user is None:
            return redirect('/')

        return render_template('manage-account.html', Name=user['Name'], Username=user['Username'],
                               Email=user['Email'])

    else:
        if request.method == "POST":
            user_to_delete = session['logged_user']['Id']
            user_found_to_delete = CleverUsers.query.filter_by(U_Id=user_to_delete).first()
            db.session.delete(user_found_to_delete)
            db.session.commit()
            flash("Your account has been successfully deleted. We are sorry to see you go.")
            return redirect('/')


@app.route('/tweety', methods=["POST", "GET"])
def talk():
    if request.method == "GET":
        return render_template('tweety.html')


if __name__ == "__main__":
    # create scrip only once

    app.run(debug=True)
