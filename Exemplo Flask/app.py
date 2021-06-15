from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello, world! CONSEGUIsss </h1>"

@app.route("/login/<nome>")
def login(nome=None):
    return "<center><h1>ola ,"+nome+"! <br />Faça seu login!</h1></center>"

@app.route("/login/<nome>")
def
if (__name__ =="__main__"):
    app.run(debug=True)