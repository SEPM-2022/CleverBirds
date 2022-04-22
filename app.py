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

 
from controllers.users_controller import * 
from controllers.game_controller import *
from controllers.user_documentation import *
from controllers.chatbot import *

#@app.get('/')
#def index_html(is_deleted=False): #  only becomes true when the function index is used
    #return render_template('index.html',variable = "Angelina",deleted_user=is_deleted)


#db.create_all()

if __name__ == "__main__":
    # create scrip only once

    app.run(debug=True)

    



