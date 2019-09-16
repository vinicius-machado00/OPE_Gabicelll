from flask import Blueprint, jsonify, request
from services.estoque_service,
import listar as service_listar, \
    localiza as service_localiza, \
    novo as service_novo, \
    remover as service_remover, \
    atualiza as service_atualiza

estoque_app = Blueprint('estoque_app', __name__, template_folder='templates')

@estoque_app.route('/estoque', methods=['GET'])
def listar():
    estoque_list = service_listar()
    return jsonify([pr.__dict__() for pr in pr_list])

#validar pelo select (Banco de dados) 
@estoque_app.route('/estoque/<int:produto>', methods=['GET'])
def localiza(produto):
    p = service_localiza(produto)
    if(p != None):
        return jsonify(p.__dict__())
    return '', 404

@estoque_app.route('/estoque', methods=['POST'])
def novo():
    novo_produto = request.get_json()
    etq_list = service_novo(novo_produto)
    return jsonify(list(map(lambda etq: etq.__dict__(), etq_list)))

@estoque_app.route('/estoque/<int:produto>', methods=['DELETE'])
def remover(estoque):
    removido = service_remover(estoque)
    if removido != None:
        return jsonify(removido.__dict__())
    return '', 404

@estoque_app.route('/estoque/<int:produto>', methods=['PUT'])
def atualiza(estoque):
    estoque_data = request.get_json()
    removido = service_atualiza(estoque, estoque_data)
    if removido != None:
        return jsonify(removido.__dict__())
    return '', 404