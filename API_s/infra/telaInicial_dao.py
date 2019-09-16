# import MySQLdb
# from Model.estoque import Estoque
import pymysql

def listarEstoque():
    resultado = []
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='RodrigoEu1')
    cursor = conexao.cursor()

    cursor.execute("select Cod_Produto, Quantidade\
        from Tab_Estoque")

    resultado = cursor.fetchall()
    # for linha in resultado :
    #     print(linha)

    conexao.commit()
    conexao.close()
    return resultado

def buscarUser(id):
    resultado = []
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='123456')
    cursor = conexao.cursor()

    # cursor.execute("select Nome_Func, Cargo, Acesso\
    #     from Tab_FUNCIONARIO where ID = :ID", {"ID": id})

    cursor.execute("select Nome_Func, Cargo, Acesso\
        from Tab_FUNCIONARIO where ID=%s", (id))

    resultado = cursor.fetchone()
    # for linha in resultado :
    #     print(linha)

    conexao.commit()
    conexao.close()
    return resultado