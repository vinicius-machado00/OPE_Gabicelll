from flask import Blueprint, jsonify, Flask, render_template, request, redirect, session, flash, url_for
from services.estoque_service import listarEstoque as service_listarEstoque, buscarUser as service_buscarUser, buscarProduto as service_buscarProduto, remover as service_remover

estoque_app = Blueprint('estoque_app', __name__, template_folder='templates')

@estoque_app.route('/estoque', methods=['GET'])
def listar():
    estoque = service_listarEventos()
    print(estoque)
    return render_template('estoque.html', titulo='GabiCell', user=user, estoque= estoque)

@estoque_app.route('/estoque/<str:nome>', methods=['GET'])
def localiza(nome):
    p = service_buscarProduto(nome)
    if(p != None): 
        return jsonify(p.__dict__())
    return '', 404

@estoque_app.route('/estoque/<int:id>', methods=['DELETE'])
def remover():
    removido = service_remover(id)
    return '', 404

@estoque_app.route('/estoque/<int:id>', methods=['PUT'])
def atualiza(matricula):
    # professor_data = request.get_json()
    # removido = service_atualiza(matricula, professor_data)
    # if removido != None:
    #     return jsonify(removido.__dict__())
    return '', 404

# @estoque_app.route('/estoque', methods=['POST'])
# def novo():
#     pr_list = service_novo(novo_professor)
#     # return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))