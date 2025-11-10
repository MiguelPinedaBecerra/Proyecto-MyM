from flask import Flask , render_template, request , redirect ,url_for ,flash

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inicio")
def pcausa():
    return render_template("inicio.html")










if __name__ == '__main__':
    app.run(debug=True)