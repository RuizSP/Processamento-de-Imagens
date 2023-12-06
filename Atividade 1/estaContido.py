n = int(input())

for i in range (n):
	A = input()
	B = input()

	#if B in A and :
		#if B[len(B) -1] == A[len(A)-1]:
	if(A.endswith(B)):
		print("encaixa")
	else:
		print("nao encaixa")
		#else:
		#print("nao encaixa")
