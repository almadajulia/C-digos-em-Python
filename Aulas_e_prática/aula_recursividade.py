def fat(n):
    if n == 0: return 1 #caso-base
    return n * fat(n-1) #caso recursivo

def fib(n):
    if n <= 1 : return n
    return fib(n-1) + fib(n-2)

N = int(input("Insira um valor para o maior N: "))

for x in range(N+1):
    print(f"{x}! = {fat(x)}")

for x in range(N+1):
    print(f"fib({x}) = {fib(x)}")