a = int(input("enter first number :\n"))
b = int(input("enter second number :\n"))
c = int(input("enter third number :\n"))

print(f'{a} is greater' if a>b and a>c else f'{b} is greater' if b>a and b>c else f'{c} is greater')