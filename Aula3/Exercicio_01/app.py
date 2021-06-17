from flask import Flask

app = Flask(__name__)

@app.route("/") #decorator
#rota para abrir o caminho(url) o / é o objeto da classe flask que vou chamar, referencia interna. rota inicial
def hello_world():
    return "<h1>Hello,Flask! Olha a vista da praia2x</h1>"

if(__name__=="__main__"):
    app.run(debug=True)