class Estoque():
    def __init__(self, cod_produto, desc_produto, quant):
        self.cod_produto = cod_produto
        self.desc_produto = desc_produto
        self.quant = quant

    def atualizar(self, dados):
        try:
            cod_produto = dados["Cod_Produto"]
            desc_produto = dados["Descricao_Produto"]
            quant = dados["Quantidade"]
            self.cod_produto, self.desc_produto, self.quant = cod_produto,desc_produto,quant
            return self
        except Exception as e:
            print("Problema ao criar novo produto no estoque!")
            print(e)

    def __dict__(self):
        d = dict()
        d['Cod_Produto '] = self.cod_produto
        d['Descricao_Produto'] = self.desc_produto
        d['Quantidade'] = self.quant
        return d

    @staticmethod
    def cria(dados):
        try:
            id = dados["id"]
            nome = dados["nome"]
            return Aluno(id=id, nome=nome)
        except Exception as e:
            print("Problema ao criar novo Aluno!")
            print(e)
    
    @staticmethod
    def cria_de_tupla(registro):
        try:
            id = registro[0]
            nome = registro[1]
            return Aluno(id=id, nome=nome)
        except Exception as e:
            print("Problema ao criar novo Aluno!")
            print(e)