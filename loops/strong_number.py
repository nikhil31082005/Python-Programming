

n = input("Enter a number : ")
l = len(n)
print(l)

sum = 0
n = int(n)
temp = n
for i in range(l):
    r = n % 10
    sum = sum + r**l
    n = n//10
    # print(sum)
if sum == temp :
    print("Strong number.")
else :
    print("Not Strong Number.")