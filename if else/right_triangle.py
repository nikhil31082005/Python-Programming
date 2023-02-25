a = int(input("Enter the first side : "))
b = int(input("Enter the second side : "))
c = int(input("Enter the third side : "))

max = a if a>b and a>c else b if b>a and b>c else c

if max**2 == a**2 + b**2 + c**2 - max**2 :
    print("Right angle triangle")

else :
    print("Not right angle triangle")