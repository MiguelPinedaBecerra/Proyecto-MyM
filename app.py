from flask import Flask , render_template, request , redirect ,url_for ,flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inicio")
def pcausa():
    return render_template("inicio.html")

@app.route("/tablas")
def pecausa():
    return render_template("tablas.html")

@app.route("/comidas")
def awowo():
    return render_template("comidas.html")

@app.route("/recetas")
def awiwi():
    return render_template("recetas.html")

@app.route("/iniciodesecion")
def awewe():
    return render_template("iniciodesecion.html")

@app.route("/Tablaimc")
def imc():
    return render_template("tablaIMC.html")

@app.route("/Tablatmb")
def imc():
    return render_template("tablaTMB.html")

@app.route("/TablaGastoc")
def imc():
    return render_template("tablaGastoC.html")

@app.route("/pesoideal")
def imc():
    return render_template("peso_ideal.html")

@app.route("/Tablamacron")
def imc():
    return render_template("tablaMacroN.html")

@app.route("/TablaRecetasP")
def imc():
    return render_template("tablarecetasPLatos.html")


if __name__ == '__main__':
    app.run(debug=True)