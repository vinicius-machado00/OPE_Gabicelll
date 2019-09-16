# from Model.estoque import Estoque
from infra.estoque_dao import listar as listar_dao, novo as novo_dao,\
    deletar as deletar_dao, atualizar as atualizar_dao,\
    listarEstoque as listarEstoque_dao, buscarUser as buscarUser_dao, buscarProduto as buscarProduto_dao

# Métodos da API 
def listarEstoque():
    return listarEstoque_dao()

def buscarUser(id):
    return buscarUser_dao(id)

def buscarProduto(nome):
    return buscarProduto_dao(id)

# Métodos da API 
def listar():
    return listar_dao()

def localiza(id):
    for p in listar_dao():
        if p.id == id:
            return p
    return None

# def novo(aluno_data):
#     # p = Aluno.cria(aluno_data)
#     # novo_dao(p.__dict__())
#     return listar_dao()

def remover(id):
    deletar_dao(id)
    return None

def atualiza(id):
    p = Aluno.cria(aluno_data)
    # atualizar_dao(id,p.__dict__())
    return atualizar_dao(id)