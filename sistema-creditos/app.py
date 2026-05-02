from flask import Flask, request, render_template_string

app = Flask(__name__)

# 🧠 base en memoria (luego pasamos a base de datos real)
users = []


@app.route("/admin")
def admin():
    return "🔐 Panel admin activo"# 🌐 HOME (USUARIO)
@app.route("/")
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Sistema Créditos</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding-top: 50px;
            }

            .box {
                background: rgba(255,255,255,0.1);
                width: 300px;
                margin: auto;
                padding: 20px;
                border-radius: 12px;
            }

            input, button {
                width: 90%;
                padding: 10px;
                margin: 5px;
                border-radius: 8px;
                border: none;
            }

            button {
                background: #22c55e;
                color: white;
            }
        </style>
    </head>

    <body>

        <h1>🏦 Sistema de Créditos</h1>

        <div class="box">
            <form method="POST" action="/register">
                <input name="name" placeholder="Nombre" required>
                <input name="phone" placeholder="Teléfono" required>
                <input name="cpf" placeholder="CPF">
                <button>Registrar</button>
            </form>
        </div>

        <br>
        <a href="/admin" style="color:white;">🔐 Panel Admin</a>

    </body>
    </html>
    """)

# 📥 REGISTRO USUARIO
@app.route("/register", methods=["POST"])
def register():
    users.append({
        "name": request.form["name"],
        "phone": request.form["phone"],
        "cpf": request.form.get("cpf", "")
    })

    return "✔ Registrado correctamente <a href='/'>volver</a>"

# 🛠 PANEL ADMIN
@app.route("/admin")
def admin():

    rows = ""
    for u in users:
        rows += f"<tr><td>{u['name']}</td><td>{u['phone']}</td><td>{u['cpf']}</td></tr>"

    return f"""
    <h1>🛠 Panel Admin</h1>

    <table border="1" style="margin:auto; background:white; color:black;">
        <tr>
            <th>Nombre</th>
            <th>Teléfono</th>
            <th>CPF</th>
        </tr>
        {rows}
    </table>

    <br>
    <a href='/'>volver</a>
    """

# 🚀 RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
