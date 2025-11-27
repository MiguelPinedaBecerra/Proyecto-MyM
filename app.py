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

def regstrar_usuario(nombre, email, password, telefono):
    try:
        cursor = mysql.connection.cursor()
        
        hashed_password = generate_password_hash(password)
        
        cursor.execute('''
            INSERT INTO users (nombre, email, password, telefono)
VALUES (%s, %s, %s, %s,)
''' (nombre, email, hashed_pasword, telefono))


mysql.connection.commit()
return True, "usuario registrado exitosamente"


@app.route('/', methods=['GET', 'POST'])
def inicio():
    nombre = session.get("nombre")
    return render_template('inicio.html', nombre=nombre)
    

@app.route('/registro', methods=['GET, 'POST']
def registro():
    if reques.method == 'POST':
    
    nombre = request.form.get('nombre')
    apellido = request.form.get('apellido')
    dia = request.form.get('dia')
    mes = request.form.get('mes')
    año = request.form.get('año')
    genero = request.form.get('genero')
    email = request.form.get('exampleInputPassword1')
    password = request.form.get('examplepassword')
    actividad = request.form.get('niveldeactividad')
    peso = request.form.get('peso')
    altura = request.form.get('altura')
    
if email in usuarios:
    flash("El correo ya esta registrado. intenta iniciar secion")
    return redirect('/iniciar_secion')
    
usuarios[email] = {
    "nombre": nombre,
    "nombre": apellido,
    "nombre": f"{dia}/{mes}/{año}",
    "nombre": genero,
    "password": password,
    "actividad": actividad,
    "peso": peso,
    "altura": altura,
    
}


with open(USUARIOS_FILE, "w") as f:
    json.dump(usuarios, f, indent=4)
    
session["usuario"] = email
session["nombre"] = nombre
session["genero"] = genero
session["actividad"] = actividad
session["peso"] = peso
session["altura"] = altura

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