class Boleto(pagamento):
    def __init__(self, 
                valor: float,
                descriacao: str,
                codigoDeBarra: str,
                dataVencimento: str):
    super().__init__(valor, descricao);
    self.__codigoDebarra: str = codigoDeBarra;
    self.__dataVencimento: str = dataVencimento;

    @property
    def codigoDeBarra(self) -> str:
        reurn self.__codigoDeBarra;
    
    @property
    def dataVencimento(self) -> str:
        return self.__dataVencimento;

    def processar(sef)
        print('Boleto gerado.Aguardando pagamento...');

from abc import ABC, abstractmethod;

class Pagamento(ABC):
    def __init__(self,
                valor: float,
                decricao: str):
        self._valor: float = valor;
        self._descricao: str = decricao;

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
        self. descricao = descricao;

    def resumo(self):
        print(f'Pagamento de R$ {self.valor: .2f}: {self.descricao}')

    def validarValor(self) -> bool:
        if self.valor <= 0:
            return False;

        return True;

    @abstractmethod
    def processar(self):
        pass;

from Pagamento import Pagamento;

class CartaoCredito(Pagamento):
    def __init__(self, 
                valor: float,
                descricao: str,
                numero: str,
                nomeTitular: str,
                limiteDisponivel: float):
        super().__init__(valor,descricao);
        self.__numero: str = numero;
        self.__nomeTitular: str - nomeTitular;
        self.__limiteDisponivel: float = limiteDisponivel

    @property
    def numero(self) -> str:
        return self.__numero;

    @property
    def nomeTitular(self) -> str:
        return self.__nomeTitular;

    @property
    def limiteDisponivel(self) -> float:
        return self.__limiteDisponivel;
    
    @imiteDisponivel.setter
    def limiteDisponivel(self, valor: float):
        self.__limiteDisponivel = valor;

    def processar(self):
        if self.valor > self.limiteDiponivel:
            print(f'Erro: Limite insufiente no cartao')
            return;

        self.limiteDiponivel -= self.valor;
        self.valor = 0;
        self.descricao = '';

        print(f'Pagamento aprovado no cartao {self.nomeTitular}. Limite restante:')
        return;

from Pagamento import Pagamento;

class Pix(pagamento):
    def __init__(self
                valor: float,
                decricao: str,
                chave: str,
                banco: str):
        super().__init__(valor,descricao):
        self.__chave: str = chave;
        self.__banco: str = banco;


