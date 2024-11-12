import random
import socket
from flask import Flask, jsonify, render_template
from pokeneas import pokeneitas

app = Flask(__name__)

@app.route('/', methods=['GET'])
def pokedex():
    return render_template('pokedex.html', pokeneas=pokeneitas, container_id=socket.gethostname())

@app.route('/pokenea', methods=['GET'])
def show_pokenea():
    pokenea = random.choice(pokeneitas)
    container_id = socket.gethostname()
    return render_template('pokeneita.html', pokenea=pokenea, container_id=container_id)

@app.route('/pokenea/<int:id>', methods=['GET'])
def show_pokenea_by_id(id):
    pokenea = next((p for p in pokeneitas if p['id'] == id), None)
    container_id = socket.gethostname()
    return render_template('pokeneita.html', pokenea=pokenea, container_id=container_id)

@app.route('/api', methods=['GET'])
def get_pokedex_api():
    return jsonify(pokeneitas)

@app.route('/api/pokenea', methods=['GET'])
def get_pokenea_api():
    pokenea = random.choice(pokeneitas)
    container_id = socket.gethostname()
    response = {
        'id': pokenea['id'],
        'nombre': pokenea['nombre'],
        'altura': pokenea['altura'],
        'habilidad': pokenea['habilidad'],
        'body': pokenea['body'],
        'card': pokenea['card'],
        'frase_filosofica': pokenea['frase_filosofica'],
        'container_id': container_id
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
