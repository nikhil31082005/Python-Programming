
n = int(input("Enter a number : "))
sum = 0

for i in range(1,n+1):
    k = int(input(f"Enter {i} number : "))
    sum = sum + k
avg = sum / n
print(f'Average of numbers is {avg}')