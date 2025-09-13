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
        ultimo_da_pilha = self.desempilhar()
        self.empilhar(ultimo_da_pilha)
        return ultimo_da_pilha
    
N = int(input())
for i in range(0,N):
    pilha = PilhaList()
    diamantes = 0
    expressao = input()
    if expressao == "":
        print(0)
    else:
        for caractere in expressao:
            if caractere == "<":
                pilha.empilhar(caractere)
            if caractere == ">" and pilha.vazia() is not True:
                pilha.desempilhar()
                diamantes += 1
        print(diamantes)