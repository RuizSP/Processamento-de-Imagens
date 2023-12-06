import math

n = int(input())

def convertMilha(a):
	milha = math.floor(a/1.609)
	return milha

for  i in range(0,n):
	a = int(input())
	milha = convertMilha(a)
	print(milha)
