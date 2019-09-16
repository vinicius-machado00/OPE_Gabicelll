# import MySQLdb # pip install mysql-python
#import pymysql # pip install pymysql 
# https://cafeinacodificada.com.br/python-mysql/
# https://imasters.com.br/desenvolvimento/conhecendo-o-jinja2-um-mecanismo-para-templates-no-flask
from Model.estoque import Estoque

def buscarProduto(nome): 
    resultado = []
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='123456')
    cursor = conexao.cursor()
    cursor.execute("select Descricao, Quantidade, Categoria, Marca, Valor\
                    from Tab_Produto where Nome=%s",(nome))
    resultado = cursor.fetchall()
    conexao.commit()
    conexao.close()
    return resultado


def deletarItemVenda(produto_id):
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='123456')
    cursor = conexao.cursor()    
    cursor.execute("delete Cod_Produto from Tab_Venda where Cod_Produto=%s",produto_id)
    conexao.commit()
    conexao.close()

def registrarVenda(produto_id):
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='123456')
    cursor = conexao.cursor()    
    cursor.execute("insert Valor_Total, Cliente, Documento_Cliente, ID_Func, Cod_Produto, Quantidade, Data from Tab_Venda")
    conexao.commit()
    conexao.close()

def buscaVenda(venda_id):
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='123456')
    cursor = conexao.cursor()    
    cursor.execute("select * from Tab_Venda where ID_Venda =%s",venda_id)
    conexao.commit()
    conexao.close()