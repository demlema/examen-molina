from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <h1>Hola desde Flask con Traefik 🚀</h1>
        <p>Bienvenido a mi aplicación Flask.</p>
        <ul>
            <li><a href="/info">Información</a></li>
            <li><a href="/tabla">Tabla simple</a></li>
            <li><a href="/lista">Lista dinámica</a></li>
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