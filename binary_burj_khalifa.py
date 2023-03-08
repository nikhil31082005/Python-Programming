n = int(input("Enter a number : "))
l = len(bin(n)[2:])
for i in range(n+1):
	x = bin(i)[2:]
	print(' '*(l-len(x)) + x)