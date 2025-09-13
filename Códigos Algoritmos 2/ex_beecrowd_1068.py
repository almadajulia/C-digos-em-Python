class PilhaList:

    def __init__(self):
        self.dados = list() #cria uma lista vazia
    
    def empilhar(self, valor):
        self.dados.append(valor)

    def desempilhar(self):
        if self.vazia():
            return None
        return self.dados.pop()
    
    def vazia(self):
        return len(self.dados) == 0

pilha = PilhaList()
linhas = []
while True:
    try:
        N = input()
        if not N:
            break
        linhas.append(N)
    except EOFError:
        break

for expressao in linhas:
    pilha = PilhaList()
    for caracter in expressao:
        if caracter == "(":
            pilha.empilhar(caracter)
        if caracter == ")" and pilha.vazia() is not True:
            pilha.desempilhar()
        elif caracter == ")" and pilha.vazia():
            pilha.empilhar("Só pra não ta mais vazia mesmo")
    if pilha.vazia():
        print("correct")
    else:
        print("incorrect")