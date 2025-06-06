# criar as rotas do nosso site (os links)
from flask import render_template, url_for, redirect
from dev import app,database
from dev.forms import Usuario


@app.route("/")
def homepage():
    
  return render_template("index.html")

@app.route("/contatos")
def contatos():
   
        return render_template('contatos.html')


@app.route("/quem")
def quem():
    return render_template("quem.html")


@app.route("/automacao")
def automacao():
    return render_template("automacao.html")

@app.route("/analise")
def analise():
    return render_template("analise.html")
   
  
@app.route("/enviar", methods=['GET', 'POST'])
def enviar():
    form_enviar= form_enviar()
    if form_enviar.validate_on_submit():

       database.session.add(Usuario)
       database.session.commit()

        

    return render_template("index.html") 

