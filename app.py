from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <h1>EXAMEN FINAL 🚀</h1>
        <p>Final aprobado, nos vemos en TITULACION</p>
        <ul>
            <li><a href="/info">Diego</a></li>
            <li><a href="/tabla">DEVOPS</a></li>
            <li><a href="/lista">TODO 10</a></li>
            <li><a href="/formulario">Formulario</a></li>
            <li><a href="/html">Página HTML completa</a></li>
            <li><a href="/api/datos">API JSON</a></li>
        </ul>
    """

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"<h2>Hola {nombre}, bienvenido a rayo.byronrm.com</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)