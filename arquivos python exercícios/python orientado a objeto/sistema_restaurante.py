from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self,nome,preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        return self._preco
    @abstractmethod
    def desc(self):
        pass


class Comida(Produto):
    
    def desc(self):
        return f'Comida: {self.nome} / preço: {self.preco}'
        

class Bebida(Produto):

    def desc(self):
        return f'Bebida: {self.nome} / preço: {self.preco}'
    
class Sobremesa(Produto):
        
    def desc(self):
        return f'Sobremesa: {self.nome} / preço: {self.preco}'
    
class Pedido:
    def __init__(self):
        self.pedidos = []

    def add(self,produto):
        self.pedidos.append(produto)

    def pagamento(self):
        total = 0
        for produto in self.pedidos:
            total += produto.preco

        return total
    
    def listar(self):
        for produto in self.pedidos:
            print(produto.desc())

class Pessoa:
    def __init__(self,nome):
        self.nome = nome
        self._pedidos=[]

    def fazer_pedido(self,pedido):
        self._pedidos.append(pedido)
        print(f'{self.nome} fez um pedido')

    def totalpessoa(self):
        totais=0
        for pedido in self._pedidos:
            x=pedido.pagamento()
            totais += x
        return totais



hamburguer = Comida('X-burguer', 15)
refri = Bebida('Coca cola', 7)
batata_frita = Comida('Batatinhas', 5)
sorvete = Sobremesa('Cascão', 6)

pedido1 = Pedido()
pedido1.add(hamburguer)
pedido1.add(batata_frita)

pedido2 = Pedido()
pedido2.add(refri)
pedido2.add(sorvete)

cliente1 = Pessoa('Diego')
cliente1.fazer_pedido(pedido1)
cliente1.fazer_pedido(pedido2)
pedido1.listar()
pedido2.listar()
print(f'Total : R${cliente1.totalpessoa()}')