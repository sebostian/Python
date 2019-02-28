#calculate fibonacci sequence using additional array A for performance
def fib(x):
	if (x==1 or x==0):
		return 1;
	if A[x] == 0:
		A[x] = fib(x-2) + fib(x-1)
	return A[x]
A = [0]*1000
print(fib(10))
