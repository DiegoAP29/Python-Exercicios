from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome, vida, mana):
        self.nome = nome
        self._vida = vida
        self._mana = mana

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            print('valor não pode ser negativo')
            return
        self._vida = valor

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, valor):
        if valor < 0:
            print('valor não pode ser negativo')
            return
        self._mana = valor

    @abstractmethod
    def atacar(self, alvo):
        pass

    def receber_dano(self, dano):
        if dano >= self.vida:
            self._vida = 0
        else:
            self._vida = self.vida - dano

    def esta_vivo(self):
        if self._vida <= 0:
            print(f'{self.nome} está morto')
        else:
            print(f'{self.nome} está com {self._vida} de vida')


class Mago(Personagem):
    def atacar(self, alvo):
        print(f'{self.nome} usou bola de fogo em {alvo.nome} causando 50 de dano!')
        alvo.receber_dano(50)
        self.mana -= 40


class Ninja(Personagem):
    def atacar(self, alvo):
        print(f'{self.nome} usou shuriken em {alvo.nome} causando 40 de dano!')
        alvo.receber_dano(40)
        self.mana -= 10


class Guerreiro(Personagem):
    def atacar(self, alvo):
        print(f'{self.nome} usou espadada em {alvo.nome} causando 30 de dano!')
        alvo.receber_dano(30)
        self.mana -= 10


Zara = Mago('Zara', 200, 200)
Kaito = Ninja('Kaito', 200, 200)
Diego = Guerreiro('Diego', 100, 100)

Zara.atacar(Diego)
Diego.esta_vivo()

Diego.atacar(Zara)
Zara.esta_vivo()

Kaito.atacar(Diego)
Kaito.atacar(Diego)
Diego.esta_vivo()