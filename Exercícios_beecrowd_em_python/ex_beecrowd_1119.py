class Pessoa:
    def __init__(self, identificador):
        self.identificador = identificador
        self.anterior = None
        self.proximo = None


def criar_lista(tamanho):
    primeira_pessoa = None
    pessoa_anterior = None

    for numero in range(1, tamanho + 1):
        nova_pessoa = Pessoa(numero)

        if primeira_pessoa is None:
            primeira_pessoa = nova_pessoa
        else:
            pessoa_anterior.proximo = nova_pessoa
            nova_pessoa.anterior = pessoa_anterior

        pessoa_anterior = nova_pessoa

    primeira_pessoa.anterior = pessoa_anterior
    pessoa_anterior.proximo = primeira_pessoa
    return primeira_pessoa


def remover_pessoa(lista, pessoa_removida):
    anterior = pessoa_removida.anterior
    proximo = pessoa_removida.proximo

    if pessoa_removida == lista:
        lista = lista.proximo
        anterior.proximo = lista
        lista.anterior = anterior
    else:
        anterior.proximo = proximo
        proximo.anterior = anterior

    return lista


def contar_pessoas(lista):
    contador = 1
    pessoa_atual = lista
    while pessoa_atual.proximo != lista:
        contador += 1
        pessoa_atual = pessoa_atual.proximo
    return contador


def andar(lista, passos, direcao):
    pessoa_atual = lista
    if direcao == 0:
        for _ in range(passos - 1):
            pessoa_atual = pessoa_atual.proximo
    else:
        for _ in range(passos - 1):
            pessoa_atual = pessoa_atual.anterior
    return pessoa_atual


while True:
    entrada = input().split()
    n, k, m = map(int, entrada)
    if n == 0:
        break

    lista = criar_lista(n)
    pessoa_k = lista
    pessoa_m = lista.anterior

    while contar_pessoas(lista) > 2:
        pessoa_k = andar(pessoa_k, k, 0)
        pessoa_m = andar(pessoa_m, m, 1)

        if pessoa_k.proximo == pessoa_m:
            proxima_k = pessoa_m.proximo
        else:
            proxima_k = pessoa_k.proximo

        if pessoa_m.anterior == pessoa_k:
            proxima_m = pessoa_k.anterior
        else:
            proxima_m = pessoa_m.anterior

        if pessoa_k == pessoa_m:
            print(f"{pessoa_m.identificador:3d},", end="")
            lista = remover_pessoa(lista, pessoa_k)
        else:
            print(f"{pessoa_k.identificador:3d}{pessoa_m.identificador:3d},", end="")
            lista = remover_pessoa(lista, pessoa_m)
            lista = remover_pessoa(lista, pessoa_k)

        pessoa_k = proxima_k
        pessoa_m = proxima_m

    if contar_pessoas(lista) == 2:
        pessoa_k = andar(pessoa_k, k, 0)
        pessoa_m = andar(pessoa_m, m, 1)

        if pessoa_k == pessoa_m:
            print(f"{pessoa_k.identificador:3d},{pessoa_k.proximo.identificador:3d}")
        else:
            print(f"{pessoa_k.identificador:3d}{pessoa_k.proximo.identificador:3d}")
    else:
        print(f"{lista.identificador:3d}")