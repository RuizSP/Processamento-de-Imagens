n = int(input())

def findAreia(a):
    return a.replace(".", "")

def findDiamante(a, contador=0):
    index = a.find("<>")
    if index != -1:
        a = a.replace("<>", "", 1)
        contador += 1
        return findDiamante(a, contador)
    return contador

for i in range(n):
    a = input()
    a = findAreia(a)
    contador = findDiamante(a)
    print(contador)
