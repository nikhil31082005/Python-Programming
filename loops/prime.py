

n = int(input("Enter a number : "))
count = 0
for i in range(1,n):
    if n%i==0 :
        count = count + 1
if count == 1 :
    print("Number is prime")
else :
    print("Number is not prime")