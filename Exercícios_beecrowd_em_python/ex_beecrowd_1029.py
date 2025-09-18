N = int(input())

for i in range(N):
    X = int(input())
    if X == 0:
        resultado = 0
        chamadas = 1
    elif X == 1:
        resultado = 1
        chamadas = 1
    else:
        fib_0 = 0
        fib_1 = 1
        chamadas_0 = 1
        chamadas_1 = 1
        
        for i in range(2, X + 1):
            resultado = fib_0 + fib_1
            chamadas = chamadas_0 + chamadas_1 + 1
            
            fib_0 = fib_1
            fib_1 = resultado
            chamadas_0 = chamadas_1
            chamadas_1 = chamadas
    
    print(f"fib({X}) = {chamadas - 1} calls = {resultado}")