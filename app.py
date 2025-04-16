from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    url = 'https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt'
    response = requests.get(url)

    personas = response.text.strip().split('\n')
    
    tabla_html = '<table border="1">'
    tabla_html += '<tr><th>ID</th><th>Nombre</th><th>Edad</th><th>Ciudad</th></tr>'
    
    for persona in personas:
        datos = persona.split(';')
        if datos[0][0] in ['3', '4', '5', '7']:
            tabla_html += f'<tr><td>{datos[0]}</td><td>{datos[1]}</td><td>{datos[2]}</td><td>{datos[3]}</td></tr>'
    
    tabla_html += '</table>'

    actual = datetime.now()
    fecha_formateada = actual.strftime("%d, %B, %Y, %M, %H, %S")
    return f'<h2>¡Hola Loja, mundo! <b>{fecha_formateada}</b></h2>' + tabla_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
