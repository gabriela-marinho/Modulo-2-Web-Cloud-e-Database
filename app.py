from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

registros = [
    {
        "id": 1,
        "nome": "Labrador",
        "imagem_url":"https://www.pngkey.com/png/detail/81-818369_labrador-retriever-transparent-image-labrador-retriever.png"
    },
    {
        "id": 2,
        "nome": "SRD",
        "imagem_url":"https://blackwhitepet.com.br/resources/img/racas-de-cachorro-vira-lata-srd.jpg"
    },
    {
        "id": 3,
        "nome": "pASTOR bELGA",
        "imagem_url":"https://www.racasdecachorro.com.br/wp-content/uploads/2018/11/sh_groenendael_495986761.jpg"
    },
]

#realizado alteraçoes
@app.route("/read")
def read_all():
    return render_template("read_all.html", registros=registros)

@app.route("/read_id/") #verificar pq esta dando erro
def read_id():
    return "Calma, se afobe não!"

@app.route("/create")
def create():
    return "Calma Maxu!"

if (__name__ == "__main__"):
    app.run(debug=True)