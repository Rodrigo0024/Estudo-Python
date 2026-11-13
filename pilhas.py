class Pilha:
    def __init__(self):
        self.items = []

    def vazio(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.vazio():
            return self.items.pop()
        else:
            raise IndexError("Voce esta tentando remover elemento de uma pilha vazia")

    def peek(self):
        if not self.vazio():
            return self.items[-1]
        else:
            raise IndexError("Voce esta tentando consultar o topo de uma pilha vazia")

    def size(self):
        return len(self.items)
minha_pilha = Pilha()
minha_pilha.push(1) 
minha_pilha.push(2)
minha_pilha.push(3)
print(minha_pilha.size())  

print(f"Consultando o topo da minha pilha: {minha_pilha.peek()}")
minha_pilha.pop()#Removendo o ultimo elemento da pilha
print(f"Consultando o topo da minha pilha: {minha_pilha.peek()}")