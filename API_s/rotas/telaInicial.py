from flask import Flask, jsonify, request
from agenda_api import agenda_app
from configuracao_api import configuracao_app
from estoque_api import estoque_app
from manutencao_api import manutencao_app
from orcamento_api import orcamento_app
from relatorio_api import relatorio_app
from venda_api import venda_app
import mysql

app = Flask(__name__)
app.register_blueprint(agenda_app)
app.register_blueprint(configuracao_app)
app.register_blueprint(estoque_app)
app.register_blueprint(manutencao_app)
app.register_blueprint(orcamento_app)
app.register_blueprint(relatorio_app)
app.register_blueprint(venda_app)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
