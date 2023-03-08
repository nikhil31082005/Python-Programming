

n = int(input("Enter a number : "))
sum = 0
for i  in range(1,n):
    if n%i==0 :
        sum = sum +i

if n == sum :
    print("Perfect number.")
else :
    print("Not Perfect number.")