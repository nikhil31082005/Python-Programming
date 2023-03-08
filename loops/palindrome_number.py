

n = input("Enter a number : ")
l = len(n)

sum = 0
n = int(n)
temp = n

for i in range(l):
    r = n % 10
    sum = (sum)*10 + r
    n = n // 10
if sum == temp :
    print("Palindrome number.")
else :
    print("Not Palindrome number.")