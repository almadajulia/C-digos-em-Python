class celula:
    def __init__(self, valor):
        self.valor = valor #preenche valor
        self.prox = None #inicialmente próximo é vazio
    def __str__(self):
        if self.prox:
            return f"{self.valor} -> " #se não é o último imprime flecha
        return f"{self.valor}." #final da lista
print("Insira valores para a lista: ")
dados = input().split()[::-1]
inicio = None #criar lista vazia
for dado in dados: #inserir dados no início da lista
    novo_item = celula(dado)
    novo_item.prox = inicio
    inicio = novo_item
def imprimir_lista(inicio):
    item_atual = inicio
    while item_atual:
        print(item_atual,end = "")
        item_atual = item_atual.prox
imprimir_lista(inicio)