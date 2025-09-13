x = int(input("Digite o dividendo: "))
y = int(input("Digite o divisor: "))
if y == 0:
    print("Erro: Divisão por zero não é permitida.")
else:
    dividendo = x
    divisor = y
    if dividendo < 0:
        dividendo = -dividendo
        
    if divisor < 0:
        divisor = -divisor

    while dividendo >= divisor:
        dividendo -= divisor
    resto = dividendo
    print(f"O resto da divisão de {x} por {y} é: {resto}")