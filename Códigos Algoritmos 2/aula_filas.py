from collections import deque

class FilaDeque:

    def __init__(self):
        self.dados = deque() #cria uma fila vazia
    
    def enfileirar(self, valor):
        self.dados.append(valor)

    def desenfileirar(self):
        if self.vazia():
            return None #se executar esse não executa o return de baixo
        return self.dados.popleft(0)
    
    def vazia(self):
        return len(self.dados) == 0
        #ou (return not self.dados)

fila = FilaDeque()
print(fila.desenfileirar())
fila.enfileirar(7)
fila.enfileirar(73)
fila.enfileirar(89)
print(fila.desenfileirar())
fila.enfileirar(3)
print(fila.desenfileirar())
fila.enfileirar(21)
fila.enfileirar(12)
print(fila.desenfileirar())

while not fila.vazia():
    print(fila.desenfileirar())

