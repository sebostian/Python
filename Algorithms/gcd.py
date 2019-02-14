def gcd(a,b):
	if (a==b):
		return a
	if (a>b):
		return gcd(a-b, b)
	else:
		return gcd(b-a, a)

def gcd_ext(a, b):
	if (b==0):
		return a
	return gcd(b, a % b)

def gcd_ext1(a, b):
	return a if b==0 else gcd(b, a % b)
		
print(gcd_ext1(14, 211))