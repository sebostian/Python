def generate_binary(M, prefix =""):
	if M==0:
		print(prefix)
		return
	generate_binary(M-1, prefix + "0")
	generate_binary(M-1, prefix + "1")


def generate_numbers(n, len, prefix):
	if len == 0:
		print(prefix)
		return 
	prefix = prefix or []
	for digit in range(n):
		prefix.append(digit)
		generate_numbers(n, len - 1, prefix)
		prefix.pop()

def find(x, str):
	for i in str:
		if i == x:
			return True
	return False

def generate_permutations(count_numbers, count_positions, prefix):
	prefix = prefix or []
	if count_positions == 0:
		print(*prefix, sep="")
		return
	for i in range(1, count_numbers +1):
		if find(i, prefix):
			continue
		prefix.append(i)
		generate_permutations(count_numbers, count_positions - 1, prefix)
		prefix.pop()

generate_binary(3)