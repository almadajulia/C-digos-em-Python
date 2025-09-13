n = int(input('Digite o número de inteiros: '))
n0 = int(input('O primeiro elemento: '))
r = int(input('Qual a razão?: '))
lista = [n0]
for i in range (0, n - 1):
    lista.append(lista[i] + r)
print(lista)