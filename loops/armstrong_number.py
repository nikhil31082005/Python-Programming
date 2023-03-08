

n = input("Enter a number : ")
l = len(n)

sum = 0
n = int(n)
p = n

for i in range(n):
    r = n % 10
    sum = sum + r**l
    n = n // 10
if sum == p :
    print("Armstrong Number.")
else :
    print("Not Armstrong Number.")