from flask import Flask , render_template, request , redirect ,url_for ,flash
from flask_mysqldb import MySQL

from werkzeug.security import generate_password_hash check_password_hash



app = Flask(__name__)
app.secret_key = 'mi_clave_secreta_super_segura'

# configuracon de MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USERNAME'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config[''MYSQL_DB]= 'usuarios_db'

MySQL = MySQL(app)

def crear_tabla():
    try:
cursor = MySQL.connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXITS usuarios (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
password VARCHAR(255) NOT NULL,
telefono VARHAR(20)
fecha_registro TIMESTAMP DEFAUL CURRENT_TIME(20)
''')

def email_existe(email);
    try:
        cursor = mysql.connection.cursor()
        cursor,execute('SELECT id FROM sers WHERE emai = %', (email,))
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"error verificando email: {e}")
        return False





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

@app.route("/TablaTMB")
def TMB():
    return render_template("tablaTMB.html")

@app.route("/TablaGastoc")
def Gc():
    return render_template("tablaGastoC.html")

@app.route("/pesoideal")
def ide():
    return render_template("peso_ideal.html")

@app.route("/Tablamacron")
def mac():
    return render_template("tablaMacroN.html")

@app.route("/TablaRecetasP")
def TBM():
    return render_template("tablarecetasPLatos.html")


if __name__ == '__main__':
    app.run(debug=True)