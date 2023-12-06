n = int(input())

global recursionCount 
recursionCount = 0

def calcFib(fib):
    global recursionCount  # Declare recursionCount como global dentro da função
    if fib == 1 or fib == 2:
        return 1
    else:
        recursionCount += 1
        return calcFib(fib - 1) + calcFib(fib - 2)

for i in range(n):
    fib = int(input())
    recursionCount = 0  # Zere recursionCount antes de calcular a sequência
    result = calcFib(fib)
    print("Fib(%d) = %d calls = %d" % (fib, recursionCount + 1, result))
