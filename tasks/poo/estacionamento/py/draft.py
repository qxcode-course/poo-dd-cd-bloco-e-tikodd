from abc import ABC, abstractmethod;
from typing import Literal;

veiculosValidos = Literal['bike', 'carro', 'moto'];

class Veiculo(ABC):
    def __init__(self,
                id: str,
                tipo: veiculosValidos,
                horaEntrada: int):
        self._id: str = id;
        self._tipo: str = tipo;
        self._horaEntrada: int = horaEntrada;

    def __str__(self) -> str:
        return f'{self.tipo.capitalize():_>10} : {self.id:_>10} : {self.horaEntrada}';

    @property
    def id(self) -> str:
        return self._id;

    @property
    def tipo(self) -> str:
        return self._tipo;

    @property
    def horaEntrada(self) -> int:
        return self._horaEntrada;

    @horaEntrada.setter
    def horaEntrada(self, hora: int):
        self._horaEntrada = hora;

    @abstractmethod
    def calcularValor(self, horaSaida:int):
        pass;

class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, 'moto', 0);

    def calcularValor(self, horaSaida: int):
        valor = (horaSaida - self.horaEntrada) / 20;
        print(f'Moto chegou {self.horaEntrada} saiu {horaSaida}. Pagar R$ {valor:.2f}');

class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, 'carro', 0);

    def calcularValor(self, horaSaida: int):
        valor = (horaSaida - self.horaEntrada) / 10;
        valorFinal = valor if valor >= 5 else 5;
        print(f'Carro chegou {self.horaEntrada} saiu {horaSaida}. Pagar R$ {valorFinal:.2f}');

class Bike(Veiculo):

    def __init__(self, id: str):
        super().__init__(id, 'bike', 0);
    
    def calcularValor(self, horaSaida: int):
        print(f'Bike chegou {self.horaEntrada} saiu {horaSaida}. Pagar R$ 3.00');

class Estacionamento:
    def __init__(self):
        self.__veiculos: dict[str, Veiculo] = {};
        self.__horaAtual: int = 0;

    def __str__(self) -> str:
        resultado = '';
        for veiculo in self.__veiculos.values():
            resultado += str(veiculo) + '\n';
        resultado += f'Hora atual: {self.__horaAtual}';
        return resultado;

    def estacionar(self, veiculo: Veiculo):
        veiculo.horaEntrada = self.__horaAtual;
        self.__veiculos[veiculo.id] = veiculo;

    def passarTempo(self, minutos: int):
        self.__horaAtual += minutos;

    def pagar(self, id: str):
        if id in self.__veiculos:
            self.__veiculos[id].calcularValor(self.__horaAtual);

    def sair(self, id: str):
        if id in self.__veiculos:
            del self.__veiculos[id];

from typing import List;

def main():
    estacionamento: Estacionamento = Estacionamento();

    while True:
        line: str = input();
        args: List[str] = line.split(' ');
        print(f'${line}');

        match args[0]:
            case 'show':
                print(estacionamento);
            case 'tempo':
                estacionamento.passarTempo(int(args[1]));

            case 'estacionar':
                match args[1]:
                    case 'bike':
                        estacionamento.estacionar(Bike(args[2]));

                    case 'moto':
                        estacionamento.estacionar(Moto(args[2]));

                    case 'carro':
                        estacionamento.estacionar(Carro(args[2]));

            case 'pagar':
                estacionamento.pagar(args[1]);
                estacionamento.sair(args[1]);

            case 'end':
                break;

            case _:
                print('Erro: comando invalido');

main();
