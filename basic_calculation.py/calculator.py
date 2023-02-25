a = float(input("Enter first number  :"))
b = float(input("Enter second number  :"))
c = input("Enter operator(+,-,*,/)")
if(c=='+'):
    print("sum of %.2f and %.2f is %.2f"%(a,b,a+b))
elif(c=='-'):
    print("substraction of %.2f from %.2f is %.2f"%(b,a,a-b))
elif(c=='*'):
    print("Multiplication of %.2f and %.2f is %.2f"%(a,b,a*b))
elif(c=='/'):
    print("division of %.2f by %.2f is %.2f"%(a,b,a/b))
else:
    print("Enter valid operator")