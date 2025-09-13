class Crianca:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
        self.ant = None
        self.prox = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def adicionar(self, crianca):
        if self.head is None:
            self.head = self.tail = crianca
            crianca.prox = crianca.ant = crianca
        else:
            self.tail.prox = crianca
            crianca.ant = self.tail
            crianca.prox = self.head
            self.head.ant = crianca
            self.tail = crianca
        self.size += 1

    def remover(self, crianca):
        if self.size == 1:
            self.head = self.tail = None
        else:
            crianca.ant.prox = crianca.prox
            crianca.prox.ant = crianca.ant
            if crianca == self.head:
                self.head = crianca.prox
            if crianca == self.tail:
                self.tail = crianca.ant
        self.size -= 1

    def get(self, index):
        current = self.head
        for _ in range(index):
            current = current.prox
        return current


import sys
input = sys.stdin.read
data = input().splitlines()

index = 0
while True:
    n = int(data[index])
    if n == 0:
        break
    index += 1
    
    lista = ListaDuplamenteEncadeada()
    for i in range(n):
        nome, valor = data[index].split()
        valor = int(valor)
        crianca = Crianca(nome, valor)
        lista.adicionar(crianca)
        index += 1

    marcados = 0
    comp = lista.get(0).valor
    n1 = n - 1
    atual = lista.head

    while marcados != n1 and n >= 2:
        if comp % 2 != 0:
            for i in range(comp):
                atual = atual.prox
        else:
            for i in range(comp):
                atual = atual.ant
        comp1 = atual.valor
        lista.remover(atual)
        marcados += 1
        n -= 1
        comp = comp1
    
    print(f"Vencedor(a): {lista.head.nome}")
