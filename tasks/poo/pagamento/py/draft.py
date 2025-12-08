class Payment:
    def__init__(self,valor: float, descricao: str)
    self.valor = valor
    self,descrição = descricao
    
    def validar_valor(self):
        i self.valor <= 0:
            raise Exception("Valor inválido para pagamento.")

    def resumo(self):
        print(f"Pagamento de R$ {self.valor}: {self.descricao}")

    def processar(self):
        pass

class CartaoCredito(Pagamento):
    def__init__(self, valor, descricao, numero, nome_titular, imite disponivel
    super().__init__(valor,descricao)
    self.numero = numero
    self. nome_titular = nome_titular
    self.limite_disponivel = limite_disponivel

    def __init__(self):
        if self.valor > self.limite_disponivel:
            raise Esception(f"Limite insuficiente no cartão {self})
    
    def processar(self):
        if self.valor > self.limite_disponivel:
            raise Exeption

    def processar (self):
        print(f"PIX enviado via {self.banco} usando chave {self.chave}
    

class Boleto(Pagamento):
    def__init__(self, valor, descricao, codig_barras, vencimento)
        super().__init__(valor, descricao)
        self.codigo_barras = codigo_barras
        self.vencimento = vencimento
    
    def processar(self):
        print("Boleto gerado. Aguardando pagamento...")

    processar_pagamento(pagamento: Pagamento):
    try:
        pagamento.validar_valor()
        pagamento.resumo()
        pagamento.processar()
    except Exception as error:
        print(f"Erro: {error}")
        print () 
if __name__ == "__main__".

     