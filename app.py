from flask import Flask, render_template,request, flash,session, redirect, url_for
import urllib
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash,check_password_hash
import time

app = Flask(__name__)

#database = 'CleverBirds_MYDB'
#username = 'sa'  
#password = '#SenhadoSA123'
 

# connection string
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=host.docker.internal;DATABASE=CleverBirds_MYDB;UID=sa;PWD=#SenhadoSA123")
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc:///?odbc_connect=%s" % params
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # para ter acesso a det dados do usuário. 
# O flask use a secret key para identificar quais cookies sao do usuário e quais nao sao 
# É como se o flask assinasse os dados do usuário com essa senha do secret key 


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
 
 
db.create_all() # assim esse comando só vai executar uma vez #


# name, username, password, email, avatar, gender

dictio = {"users":[]}

#==> Rota de cadastro de usuário (MINHA VERSAO 2)
@app.route('/signup', methods=["POST", "GET"]) 
def page_signup():
    if request.method=="POST":
        dados=request.form.to_dict()
        dictio["users"].append(dados)
        # Generating password hash
        password_hash= generate_password_hash(dados.get('password'))
        # testing to see if the user creating is working:  
        new_user=CleverUsers(U_Name= dados.get('name'),U_Username=dados.get('username'),U_Password= password_hash,U_Email=dados.get('email'),U_Score=dados.get('score'), U_CharacterName=dados.get('avatar'),U_Gender=dados.get('gender'))
        db.session.add(new_user)
        #precisa de commit para inserir 
        db.session.commit()
        return render_template('signup-success.html')
    if request.method=="GET":
        return render_template('create-account.html') # Aqui eh q o GET acontece (é o else do if da linha 62)
       
   #     return render_template('create-account.html')

#==> Rota de login ( VERSAO 3)
@app.route('/login', methods=["POST", "GET"]) 
def page_login():
    if request.method=="POST":
        dados=request.form.to_dict()
        dictio["users"].append(dados)
        #print(dados)
        # to check is the password is correct what we do is: check_password_hash(hash," - senha recebida p/ verificação - ")
        user_found = CleverUsers.query.filter_by(U_Username= dados.get('username')).first()  # vai retornar o usuário 
        print(user_found)
        if user_found == None:
            print("User not found")
            return render_template('index.html',user_not_found=True) #using JInja in index.html
        else:
            if check_password_hash(user_found.U_Password, dados.get('password')): #essa funcao recebe o hash q quero verificar e a segunda eh a senha q o usuário digitou 
                print("Usuário logado")
                # A chave agora está recebendo um dicionário para poder usar na rota do manage account
                session['logged_user'] = {'Name': user_found.U_Name,
                'Username':  user_found.U_Name,
                'Avatar':  user_found.U_CharacterName,
                'Score':user_found.U_Score,
                'Email':user_found.U_Email,
                'Id': user_found.U_Id
                }
                  # armazenando o userfound na chave "logged user" do dicionario session. Esse dicionário é unico para cada usuário. Depois disso já posso usar em outra rota
                return render_template('user-dashboard.html', Name = user_found.U_Name, Username = user_found.U_Username, Avatar=user_found.U_CharacterName, Score=user_found.U_Score )
    if request.method=="GET":
        return render_template('index.html',user_not_found=False)  

#==> Rota de jogo  
@app.route('/playgame', methods=["POST", "GET"]) 
def playing_game():
    if request.method=="GET":
        return render_template('playgame.html')  



#==> Rota para about  
@app.route('/about', methods=["POST", "GET"]) 
def about():
    if request.method=="GET":
        return render_template('about.html')  

#==> Rota para o privacy policy  
@app.route('/privacy', methods=["POST", "GET"]) 
def privacy():
    if request.method=="GET":
        return render_template('privacy-policy.html')  


#==> Rota para mudar avatar 
@app.route('/changeavatar', methods=["POST", "GET"]) 
def change_avatar():
### inserir o post 
    if request.method=="GET":
        return render_template('change-avatar.html') 


#==> Rota para manage account  
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
            return index_html(True)

# return redirect(url_for('/', deleted_user=True))
#  return ('manage-account.html', deleted_user=True) 
#==> Rota para talk to Tweety  
@app.route('/tweety', methods=["POST", "GET"]) 
def talk():
    if request.method=="GET":
        return render_template('tweety.html')  

@app.get('/')
def index_html(is_deleted=False): # fica falso por padrao e se torna true na linhe 150 quando é feito o redicionamento chamando a funcao index.
    return render_template('index.html',variable = "Angelina",deleted_user=is_deleted)

if __name__== "__main__":
    # create scrip only once
     
    app.run(debug=True)


 