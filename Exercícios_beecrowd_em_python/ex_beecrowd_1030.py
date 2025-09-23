NC = int(input())

for caso in range(1, NC + 1):
    n, k = map(int,input().split())
    pessoas = []
    for i in range(1, n + 1):
        pessoas.append(i)

    indice = 0

    while len(pessoas) > 1:
        indice = (indice + k - 1) % len(pessoas)
        pessoas.pop(indice)

    sobrevivente = pessoas[0]

    print(f"Case {str(caso)}: {str(sobrevivente)}")