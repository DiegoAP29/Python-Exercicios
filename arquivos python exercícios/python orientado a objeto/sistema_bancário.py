from abc import ABC, abstractmethod

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.lista_contas = []

    def add_conta(self,conta):
        self.lista_contas.append(conta)
        print(f'conta de número {conta.numero_conta} adicionada')

    def listar_contas(self):
        print(f'contas de {self.nome}: ')
        for contas in self.lista_contas:
            print(contas.numero_conta)


class Conta(ABC):
    def __init__(self, titular, saldo, numero_conta):
        self.titular = titular
        self._saldo = saldo
        self.numero_conta = numero_conta


    @abstractmethod
    def sacar(self, saque):
        pass

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f'depósito de R${valor} feito, saldo é R${self._saldo}')
        elif valor == 0:
            print('nada adicionado no saldo da conta')
        else:
            print('valor inválido, nada depositado')

    def mostrar_saldo(self):
        print(f'saldo é R${self._saldo}')

    def transferir(self, alvo, valor):
        if valor > self._saldo:
            print('operação inválida')
            return
        
        self._saldo -= valor
        alvo._saldo += valor

        print(f'saldo da conta após retirada {self._saldo}/saldo da outra conta após depósito é R${alvo._saldo}')



class ContaCorrente(Conta):

    def sacar(self, saque):
        if saque > self._saldo:
            print('operação inválida')
            return
        
        self._saldo = self._saldo - saque - 2

        print(f'após o saque de R${saque} o saldo agora é R${self._saldo}')

class ContaPoupanca(Conta):
    
    def sacar(self, saque):
        if saque > self._saldo:
            print('operação inválida')
            return
        
        self._saldo -= saque
        print(f'após o saque de R${saque} o saldo agora é R${self._saldo}')

diego = Cliente('Diego')
c1 = ContaCorrente('Diego', 100, 123)
c2 = ContaPoupanca('Diego', 100, 124)
diego.add_conta(c1)
diego.add_conta(c2)
c1.depositar(500)
c1.transferir(c2,100)
c2.sacar(50)
diego.listar_contas()