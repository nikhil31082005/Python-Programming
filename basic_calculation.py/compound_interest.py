p = float(input("Enter the principle amount :\n"))
r = float(input("Enter the rate :\n"))
t = float(input("Enter the time in year :\n"))

A = p*((1+(r/100))**t)

compound_interest = A - p

print("Amount :",A)

print("C.I :",compound_interest)