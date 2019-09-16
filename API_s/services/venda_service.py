# from Model.estoque import Estoque
from infra.venda_dao import buscarProduto as buscarProduto_dao, deletarItemVenda as deletarItemVenda_dao, registrarVenda as registrarVenda_dao, buscaVenda as buscaVenda_dao

# Métodos da API 
def buscarProduto(nome):
    return buscarProduto_dao(nome)

def deletarItemVenda(produto_id):
    return deletarItemVenda_dao(produto_id)

def registrarVenda(valor_total,cliente,documento_cliente,id_func,cod_produto,quantidade): 
    return registrarVenda_dao(valor_total,cliente,documento_cliente,id_func,cod_produto,quantidade)

def buscaVenda(id_venda): 
    return buscaVenda_dao(id_venda)




# def novo(aluno_data):
#     # p = Aluno.cria(aluno_data)
#     # novo_dao(p.__dict__())
#     return listar_dao()

# def atualiza(id):
#     p = Aluno.cria(aluno_data)
#     # atualizar_dao(id,p.__dict__())
#     return atualizar_dao(id)