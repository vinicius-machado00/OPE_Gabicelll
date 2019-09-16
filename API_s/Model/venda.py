class Venda():
    def __init__(self,valor_total,cliente,documento_cliente,id_func,cod_produto,quantidade):
        self.valor_total = valor_total
        self.cliente = cliente
        self.documento_cliente = documento_cliente
        self.id_func = id_func
        self.cod_produto = cod_produto
        self.quantidade = quantidade

    # def atualizar(self, dados):
    #     try:
    #         cod_produto = dados["Cod_Produto"]
    #         desc_produto = dados["Descricao_Produto"]
    #         quant = dados["Quantidade"]
    #         self.cod_produto, self.desc_produto, self.quant = cod_produto,desc_produto,quant
    #         return self
    #     except Exception as e:
    #         print("Problema ao criar novo produto no estoque!")
    #         print(e)

    def __dict__(self):
        d = dict()
        d["valor_total"] = self.valor_total
        d["cliente"] = self.cliente
        d["documento_cliente"] = self.documento_cliente
        d["id_func"] = self.id_func
        d["cod_produto"] = self.cod_produto
        d["quantidade"] = self.quantidade
        return d

    @staticmethod
    def cria(dados):
        try:
            valor_total = dados["valor_total"]
            cliente = dados["cliente"]
            documento_cliente = dados["documento_cliente"]
            id_func = dados["id_func"]
            cod_produto = dados["cod_produto"]
            quantidade = dados["quantidade"]
            return Venda(valorTotal=valor_total,cliente=cliente,documento_cliente=documento_cliente,id_func=id_func,cod_produto=cod_produto,quantidade=quantidade)
        except Exception as e:
            print("Problema ao registar nova Venda! ")
            print(e)
    
    @staticmethod
    def cria_de_tupla(registro):
        try:
            valor_total = registro[0]
            cliente = registro[1]
            documento_cliente = registro[2]
            id_func = registro[3]
            cod_produto = registro[4]
            quantidade = registro[5]
            return Venda(valorTotal=valor_total,cliente=cliente,documento_cliente=documento_cliente,id_func=id_func,cod_produto=cod_produto,quantidade=quantidade)
        except Exception as e:
            print("Problema ao criar nova Venda !")
            print(e)