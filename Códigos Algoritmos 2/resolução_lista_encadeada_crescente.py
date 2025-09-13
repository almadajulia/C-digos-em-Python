class celula:
    def __init__(self, valor):
        self.valor = valor #preenche valor
        self.prox = None #inicialmente próximo é vazio
    def __str__(self):
        if self.prox:
            return f"{self.valor} -> " #se não é o último imprime flecha
        return f"{self.valor}." #final da lista
    
def inserir_item_em_ordem(inicio, valor):
    novo_item = celula(valor)
    if inicio == None: return novo_item
    if valor < inicio.valor:
        novo_item.prox = inicio
        return novo_item
    item_atual = inicio
    while item_atual:
        if item_atual.prox == None or item_atual.prox.valor > valor: #buscar posição correta
            novo_item.prox = item_atual.prox
            item_atual.prox = novo_item
            break
        item_atual = item_atual.prox
    return inicio

print("Insira valores para a lista: ")
dados = input().split()[::-1]
inicio = None #criar lista vazia

for dado in dados:
    inicio = inserir_item_em_ordem(inicio, int(dado))

def imprimir_lista(inicio):
    item_atual = inicio
    while item_atual: #enquanto item_atual for diferente de None
        print(item_atual,end = "")
        item_atual = item_atual.prox
imprimir_lista(inicio)
#para definir a ordem crescente tinha que achar o item maior que o número analisado para encaixar esse número