# crianndo arquivo de inicialzacao de ambiente

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbsite.db'
app.config['SCERET_KEY']= "6b562dc96df740a648347938a29cdc23" 

database=SQLAlchemy(app)
bcrypt = Bcrypt(app)




login_manager=LoginManager(app)
login_manager.login_view ="homepage"



from dev import routes


