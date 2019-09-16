from flask import Blueprint, jsonify, Flask, render_template, request, redirect, session, flash, url_for
from services.telaInicial_service import listarEstoque as service_listarEstoque, buscarUser as service_buscarUser

telaInicial_app = Blueprint('telaInicial_app', __name__, template_folder='templates')

@telaInicial_app.route('/home', methods=['GET'])
def listar():
    user = service_listarEstoque()
    estoque = service_buscarUser(1)
    return render_template('home.html', titulo='GabiCell', user=user, estoque= estoque)

@telaInicial_app.route('/professores/<int:matricula>', methods=['GET'])
def localiza(matricula):
    # p = service_localiza(matricula)
    # if(p != None):
    #     return jsonify(p.__dict__())
    return '', 404

@telaInicial_app.route('/professores', methods=['POST'])
def novo():
    novo_professor = request.get_json()
    # print('Teste de envio da requisicao em professores/ POST')
    # print(novo_professor)
    # pr_list = service_novo(novo_professor)
    # return jsonify(list(map(lambda pr: pr.__dict__(), pr_list)))

@telaInicial_app.route('/professores/<int:matricula>', methods=['DELETE'])
def remover(matricula):
    # removido = service_remover(matricula)
    # if removido != None:
    #     return jsonify(removido.__dict__())
    return '', 404

@telaInicial_app.route('/professores/<int:matricula>', methods=['PUT'])
def atualiza(matricula):
    # professor_data = request.get_json()
    # removido = service_atualiza(matricula, professor_data)
    # if removido != None:
    #     return jsonify(removido.__dict__())
    return '', 404