from flask import Blueprint,render_template

app_blueprint = Blueprint('app_blueprint',__name__)

@app_blueprint.route("/") #decorator
#rota para abrir o caminho(url) o / é o objeto da classe flask que vou chamar, referencia interna. rota inicial
def hello_world():
    return "<h1>Hello,Flask! Olha a vista da praiaxp</h1>"

#ROTA 2
@app_blueprint.route("/rota2/<nome>") #decorator

def rota2(nome=None):
    return "<h1>Hello, "+nome+"! </h1><h3> Olha a rota 2</h3>"

@app_blueprint.route("/exemplo") #decorator
def rota3():
    return render_template('aula2_ex1.html')