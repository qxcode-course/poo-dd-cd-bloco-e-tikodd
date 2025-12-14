from abc import ABC, abstractmethod;

class Animal (ABC):
    def __init__(self, nome: str = 'criatura'):
        self._nome: str = nome;

    @property
    def nome(self) -> str:
        return self._nome;

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome;

    def apresentarNome(self):
        print(f'eu sou um(a) {self.nome}');

    @abstractmethod
    def fazerSom(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Cachorro(Animal):
    def __init__(self, nome: str):
        super().__init__(nome);

    def fazerSom(self):
        print('Au au au!');

    def mover(self):
        print(f'O cachorro {self.nome} está correndo');

class Urso(Animal):
    def __init__(self, nome: str):
        super().__init__(nome);

    def fazerSom(self):
        print('uar!');

    def mover(self):
        print(f'O urso {self.nome} está comendo mel');

class Sapo(Animal):
    def __init__(self, nome: str):
        super().__init__(nome);

    def fazerSom(self):
        print('uebete uebete!');

    def mover(self):
        print(f'O sapo {self.nome} está pulando');


cachorro: Cachorro = Cachorro('Caramelo');
urso: Urso = Urso('Baloo');
sapo: Sapo = Sapo('Xena');

def apresentarAnimal(animal: Animal):
    print(f'=====[{type(animal).__name__}]=====');
    animal.apresentarNome();
    animal.fazerSom();
    animal.mover();
    print(f'=====[{type(animal).__name__}]=====\n');

listaAnimais = [cachorro, urso, sapo];
for animal in listaAnimais:
    apresentarAnimal(animal);
    




