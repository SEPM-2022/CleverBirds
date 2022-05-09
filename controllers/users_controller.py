
from flask import Flask, render_template, request, session, make_response
from app import app, db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from models.clever_users import *


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
    if request.method=="POST":
        dados=request.form.to_dict() 
        #print(dados)
        # to check is the password is correct what we do is: check_password_hash(hash," - received password for verification - ")
        user_found = CleverUsers.query.filter_by(U_Username= dados.get('username')).first()  # vai retornar o usuário 
        print(user_found)
        if user_found == None:
            print("User not found")
            return render_template('index.html',user_not_found=True) #using JInja in index.html
        else:
            if check_password_hash(user_found.U_Password, dados.get('password')): # this function receives a hash to compare with what the user typed
                print("User Logged in")
                # The key is now receiving a dic to be used in the manage account route  
                session['logged_user'] = {'Name': user_found.U_Name,
                'Username':  user_found.U_Name,
                'Avatar':  user_found.U_CharacterName,
                'Score':user_found.U_Score,
                'Email':user_found.U_Email,
                'Id': user_found.U_Id
                }
                  # Storing userfound in the key "logged user" of the session dic. After this I can use it in another route. 
                return render_template('user-dashboard.html', Name = user_found.U_Name, Username = user_found.U_Username, Avatar=user_found.U_CharacterName, Score=user_found.U_Score )
            else:
                flash("Wrong username/password.")
    if request.method=="GET":
        return render_template('index.html',user_not_found=False)  



@app.route('/changeavatar', methods=["POST", "GET"])
def change_avatar():
    if request.method == "GET":
        return render_template('change-avatar.html')


@app.route('/useraccount', methods=["POST", "GET"])
def manageAccount():
    if request.method=="GET":
        # o user_found agora é um dicionário
        user_found = session['logged_user']
        return render_template('manage-account.html', Name = user_found['Name'], Username = user_found['Username'],Email = user_found['Email'])  

    else:
        if request.method=="POST":
            # Vou deletar o campo Id do session['logged_user']
            # Documentation => https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/
 
            user_to_delete = session['logged_user']['Id']  

            user_found_to_delete = CleverUsers.query.filter_by(U_Id= user_to_delete).first() #fazendo query no banco para pegar o user Id
            db.session.delete(user_found_to_delete)
            db.session.commit()
            return render_template('index.html', deleted_user=True)
