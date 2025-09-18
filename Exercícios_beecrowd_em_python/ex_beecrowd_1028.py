def MDC(a, b):
    if b == 0: return a
    return MDC(b, a % b)
    
N = int(input())
for i in range(0, N):
    F1, F2 = map(int, input().split())
    print(MDC(F1, F2))