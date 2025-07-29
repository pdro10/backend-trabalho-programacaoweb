from flask_cors import CORS
from flask import Flask, request, jsonify
#from config import Config

# onde será construido os endpoints e suas logicas internas de processamentos

app = Flask(__name__)
CORS(app)
#app.config.from_object(Config)

@app.route('/listacategorias', methods= ['GET'])
def listacategorias():
    categorias = ["arroz", "açucar"]

    return jsonify(categorias), 200

#listagem de produtos filtrando por categorias usando id como parametro
@app.route('/listagemprodutos', methods= ['GET'])
def listagemprodutos():
    produtos = ["arroz", "café", "miojo"]

    return jsonify(produtos)

@app.route('/'. methods= [])


if __name__ == '__main__':
    app.run(debug=True)