x = int(input("Digite o dividendo: "))
y = int(input("Digite o divisor: "))

if y == 0:
    print("Erro: Divisão por zero não é permitida.")
else:
    resultado = 0
    dividendo = x
    divisor = y
    if dividendo < 0:
        dividendo = -dividendo
    if divisor < 0:
        divisor = -divisor

    while dividendo >= divisor:
        dividendo -= divisor
        resultado += 1
    if (x < 0 and y > 0) or (x > 0 and y < 0):
        quociente = -resultado

    print(f"O resultado da divisão de {x} por {y} é: {resultado}")