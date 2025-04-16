import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    respuesta = requests.get(url)
    contenido = respuesta.text.splitlines()
    personas = []
    for linea in contenido:
        if linea.startswith(('3', '4', '5', '7')):
            partes = linea.split(',')
            persona = {
                'id': partes[0],
                'nombre': partes[1],
                'apellido': partes[2],
                'edad': partes[3]
            }
            personas.append(persona)
    
    html = '''
    <html>
        <head>
            <title>Lista de Personas</title>
        </head>
        <body>
            <h1>Lista de Personas</h1>
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Edad</th>
                </tr>'''
    for persona in personas:
        html += f'''
                <tr>
                    <td>{persona['id']}</td>
                    <td>{persona['nombre']}</td>
                    <td>{persona['apellido']}</td>
                    <td>{persona['edad']}</td>
                </tr>'''
    html += '''
            </table>
        </body>
    </html>'''
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)