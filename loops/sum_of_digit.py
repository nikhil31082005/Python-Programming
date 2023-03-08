

n = int(input("Enter a number : "))
sum = 0
for i in range(1,n):
    r = n%10
    sum = sum + r
    n = n//10
print(sum)