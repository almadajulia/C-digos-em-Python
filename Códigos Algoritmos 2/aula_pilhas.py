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