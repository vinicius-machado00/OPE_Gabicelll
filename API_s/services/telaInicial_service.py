# from Model.estoque import Estoque
from infra.telaInicial_dao import listarEstoque as listarEstoque_dao, buscarUser as buscarUser_dao

# Métodos da API 
def listarEstoque():
    return listarEstoque_dao()

def buscarUser(id):
    return buscarUser_dao(id)