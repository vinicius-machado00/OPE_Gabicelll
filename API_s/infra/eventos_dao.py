# import MySQLdb # pip install mysql-python
#import pymysql # pip install pymysql 
# https://cafeinacodificada.com.br/python-mysql/
# https://imasters.com.br/desenvolvimento/conhecendo-o-jinja2-um-mecanismo-para-templates-no-flask
from Model.estoque import Estoque

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
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='RodrigoEu1')
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

def buscarProduto(nome): 
    resultado = []
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='RodrigoEu1')
    cursor = conexao.cursor()

    cursor.execute("select Descricao, Quantidade, Categoria, Marca, Valor\
                    from Tab_Produto where Nome=%s",(nome))
    
    resultado = cursor.fetchall()
    conexao.commit()
    conexao.close()
    return resultado

def listar():
    resultado = []
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='RodrigoEu')
    cursor = conexao.cursor()

    cursor.execute("select Cod_Produto, Quantidade\
        from Tab_Estoque")

    resultado = cursor.fetchall()
    # for linha in resultado :
    #     print(linha)

    conexao.commit()
    conexao.close()
    return resultado

def novo(aluno_dicionario):
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='RodrigoEu')
    cursor = conexao.cursor()  
    cursor.execute("insert into alunos (nome)\
        values(:nome)", aluno_dicionario)
    conexao.commit()
    conexao.close()

def deletar(produto_id):
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='RodrigoEu')
    cursor = conexao.cursor()    
    cursor.execute("delete from Tab_Estoque\
        where id = :id", {"id":produto_id})
    conexao.commit()
    conexao.close()

def atualizar(produto_id, aluno_dicionario):
    conexao = pymysql.connect(db='DB_GabbiCell', user='root', passwd='RodrigoEu')
    cursor = conexao.cursor()   
    aluno_dicionario['aluno_id'] = produto_id
    cursor.execute("update from alunos\
        set nome = :nome where id = :aluno_id ", aluno_dicionario)
    conexao.commit()
    conexao.close()