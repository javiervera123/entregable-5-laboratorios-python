from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    nombre = request.form.get("nombre")
    saludo = f"Hola, {nombre}! Bienvenido."
    return saludo

if __name__ == "__main__":
    app.run(debug=True)