
# Алгоритм поиска длины НОПП с запоминанием

def nopp(A, B):
	na = len(A)
	nb = len(B)

	# Массив для промежуточных вычислений
	# D[i][j] = D(A[0..i], B[0..j])
	D = [[None]*(nb+1) for i in range(na+1)]

	for i in range(na+1):
		for j in range(nb+1):
			if i == 0 or j == 0 :
				D[i][j] = 0
			elif A[i-1] == B[j-1]:
				D[i][j] = 1 + D[i-1][j-1]
			else:
				D[i][j] = max(D[i-1][j] , D[i][j-1])

	return D[na][nb]

# Тест
A = 'SEQUENCE'
B = 'SUCCESS'
print(nopp(A, B))
