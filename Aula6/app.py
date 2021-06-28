from flask import Flask, render_template, request

app = Flask(__name__)
#METODO POST vai no corpo da requisição
#METODO GET atraves da url passa os parametros do formulario
@app.route("/", methods=('GET', 'POST')) # rota, metodos :get e post(enviar a informaçao)
def index():
    nome = None #variaveis vazias qnd clicar em jogar submete atraves do metodo get
    sobrenome = None #variaveis
    criatura = None #variaveis
    imagem = None #variaveis
    #request captura uma informação,verifica se a pagina está sendo recarregada pelo metodo get ou post
    if request.method == 'POST': #pergunta: se eu estiver recebendo uma info(recarregzndo a pagina),com o requisito post
        # se for requisitado o metodo ele pega as variaveis
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        criatura = request.form['criatura']

        if criatura == "ELFO":
            imagem = "https://i.pinimg.com/originals/52/b8/c3/52b8c320e93e722020f51d6e4920d6bc.gif" # imagem de elfo
        elif criatura == "ORC":
            imagem = "https://thumbs.gfycat.com/ExemplarySeriousBeardedcollie-max-1mb.gif" # imagem do orc
        elif criatura == "HOBBIT":
            imagem = "https://media.tenor.com/images/a758b5c5a136dde219fc5926b42c7b1b/tenor.gif" # imagem do hobbit
        else:
            imagem = None #padrão de imagem é vazio por isso o else é imagem none

    return render_template("index.html", nome=nome, sobrenome=sobrenome, criatura=criatura, imagem=imagem)
    #acima,passando os parametros pelo render templete 
if (__name__ == "__main__"):
    app.run(debug=True)