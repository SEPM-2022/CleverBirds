from flask import Flask, render_template,request 
import urllib
from flask_sqlalchemy import SQLAlchemy 
 

app = Flask(__name__)

#database = 'CleverBirds_MYDB'
#username = 'sa'  
#password = '#SenhadoSA123'
 

# connection string
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=host.docker.internal;DATABASE=CleverBirds_MYDB;UID=sa;PWD=#SenhadoSA123")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params

db = SQLAlchemy(app)

class CleverUsers(db.Model):
    U_Id = db.Column(db.Integer, primary_key=True)
    U_Name = db.Column(db.String(20), unique=False, nullable=False)
    U_Username = db.Column(db.String(20), unique=False, nullable=False)
    U_Password = db.Column(db.String(20), unique=False, nullable=False)
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
 
 
#db.create_all() # execute one time


# name, username, password, email, avatar, gender

dictio = {"users":[]}

#==> Route to create an account
@app.route('/signup', methods=["POST", "GET"]) 
def page_signup():
    if request.method=="POST":
        dados=request.form.to_dict()
        dictio["users"].append(dados)
        # testing to see if the user creating is working:  
        new_user=CleverUsers(U_Name= dados.get('name'),U_Username=dados.get('username'),U_Password=dados.get('password'),U_Email=dados.get('email'),U_Score=dados.get('score'), U_CharacterName=dados.get('avatar'),U_Gender=dados.get('gender'))
        db.session.add(new_user)
        db.session.commit()
        return render_template('signup-success.html')
    if request.method=="GET":
        return render_template('create-account.html') # Aqui eh q o GET acontece (é o else do if da linha 62)
       
   #     return render_template('create-account.html')


@app.get('/')
def index_html():
    return render_template('draft.html',variable = "Angelina")

if __name__== "__main__":
    # create scrip only once
     
    app.run(debug=True)





 

