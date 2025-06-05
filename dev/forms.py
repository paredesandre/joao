
# criar os formularios do nosso site
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from dev.models import Usuario



class FormEnviar(FlaskForm):
    email    = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário ", validators=[DataRequired()])
    fone     = StringField("Numero Telefone ", validators=[DataRequired()])
    Assunto  = StringField("Assunto/Problema ", validators=[DataRequired()])
    botao_Enviar = SubmitField("Enviar")



                      


