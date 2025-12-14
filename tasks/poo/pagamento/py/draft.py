from abc import ABC, abstractmethod;

class Pagamento(ABC):
    def __init__(self,
                valor: float,
                descricao: str):
        self._valor: float = valor;
        self._descricao: str = descricao;

    @property
    def valor(self) -> float:
        return self._valor;

    @property
    def descricao(self) -> str:
        return self._descricao;

    @valor.setter
    def valor(self, valor: float):
        self._valor = valor;

    @descricao.setter
    def descricao(self, descricao: str):
        self._descricao = descricao;

    def resumo(self):
        print(f'Pagamento de R$ {self.valor: .2f}: {self.descricao}')

    def validarValor(self) -> bool:
        if self.valor <= 0:
            return False;

        return True;

    @abstractmethod
    def processar(self):
        pass;

class Boleto(Pagamento):
    def __init__(self, 
                valor: float,
                descricao: str,
                codigoDeBarra: str,
                dataVencimento: str):
        super().__init__(valor, descricao);
        self.__codigoDeBarra: str = codigoDeBarra;
        self.__dataVencimento: str = dataVencimento;

    @property
    def codigoDeBarra(self) -> str:
        return self.__codigoDeBarra;
    
    @property
    def dataVencimento(self) -> str:
        return self.__dataVencimento;

    def processar(self):
        print('Boleto gerado.Aguardando pagamento...');

class CartaoCredito(Pagamento):
    def __init__(self, 
                valor: float,
                descricao: str,
                numero: str,
                nomeTitular: str,
                limiteDisponivel: float):
        super().__init__(valor,descricao);
        self.__numero: str = numero;
        self.__nomeTitular: str = nomeTitular;
        self.__limiteDisponivel: float = limiteDisponivel;

    @property
    def numero(self) -> str:
        return self.__numero;

    @property
    def nomeTitular(self) -> str:
        return self.__nomeTitular;

    @property
    def limiteDisponivel(self) -> float:
        return self.__limiteDisponivel;
    
    @limiteDisponivel.setter
    def limiteDisponivel(self, valor: float):
        self.__limiteDisponivel = valor;

    def processar(self):
        if self.valor > self.limiteDisponivel:
            print(f'Erro: Limite insuficiente no cartao')
            return;

        self.limiteDisponivel -= self.valor;
        self.valor = 0;
        self.descricao = '';

        print(f'Pagamento aprovado no cartao {self.nomeTitular}. Limite restante:')
        return;

class Pix(Pagamento):
    def __init__(self,
                valor: float,
                descricao: str,
                chave: str,
                banco: str):
        super().__init__(valor,descricao);
        self.__chave: str = chave;
        self.__banco: str = banco;

    @property
    def chave(self) -> str:
        return self.__chave;

    @property
    def banco(self) -> str:
        return self.__banco;

    def processar(self):
        self.valor = 0;
        self.descricao = '';

        print(f'PIX enviado via {self.banco} usando chave {self.chave}');
        return;

pagamentos = [
    Pix(150, 'Camisa esportiva', 'email@ex.com', 'Banco XPTO'),
    CartaoCredito(400, 'Tênis esportivo', '1234 5678 9123 4567', 'Cliente X', 500),
    Boleto(89.90, 'Livro de Python', '123456789000', '2025-01-10'),
    CartaoCredito(800, 'Notebook', '9999 8888 7777 6666', 'Cliente Y', 700),  # deve falhar
];

# Método processarPagamento
def processarPagamento(pagamento: Pagamento):
  if pagamento.validarValor() is False:
    print('Erro: pagamento invalido');
    return;

  pagamento.resumo();
  pagamento.processar();

  return;

# Processando instâncias de pagamentos
for pagamento in pagamentos:
  processarPagamento(pagamento);
