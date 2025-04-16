import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    respuesta = requests.get(url)
    lineas = respuesta.text.splitlines()
    
    personas = []

    for linea in lineas[1:]:
        if linea.startswith(('3', '4', '5', '7')):
            partes = linea.split('|')
            personas.append(partes)
    personas.sort(key=lambda x: x[0])

    html = '''
    <html>
        <body>
            <h1>Actividad Experimental Semana02</h1>
            <table border="1">
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>País</th>
                    <th>Dirección</th>
                </tr>'''
    for persona in personas:
        html += f'''
                <tr>
                    <td>{persona[0]}</td>
                    <td>{persona[1]}</td>
                    <td>{persona[2]}</td>
                    <td>{persona[3]}</td>
                    <td>{persona[4]}</td>
                </tr>'''
    html += '''
            </table>
        </body>
    </html>'''
    
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
