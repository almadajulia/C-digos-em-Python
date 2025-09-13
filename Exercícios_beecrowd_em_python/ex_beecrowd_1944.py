class PilhaList:

    def __init__(self):
        self.dados = list()
    
    def empilhar(self, valor):
        self.dados.append(valor)

    def desempilhar(self):
        if self.vazia():
            return None
        return self.dados.pop()
    
    def vazia(self):
        return len(self.dados) == 0
    
    def verificar_o_ultimo(self):
        if self.vazia():
            return None
        return self.dados[-1]
    
    def tamanho_da_pilha(self):
        return len(self.dados)

N = int(input())
pilha = PilhaList()
brindes = 0
pilha.empilhar(["F", "A", "C", "E"])
for i in range (0, N):
    combinação_das_letras = list(input().split())
    ultimo_da_pilha = pilha.verificar_o_ultimo()
    if combinação_das_letras == list(reversed(ultimo_da_pilha)):
        if pilha.tamanho_da_pilha() != 1:
            pilha.desempilhar()
        brindes += 1
    else:
        pilha.empilhar(combinação_das_letras)
print(brindes)