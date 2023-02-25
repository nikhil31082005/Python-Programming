amount = int(input("Enter the amount :\n"))

if amount>=25000 :
    print("Gold catagory.")
    discount = (amount * 20)/100
    amount_payable = amount - discount
    print(f"Amount payable is {amount_payable}")

elif amount >= 10000 and amount <25000 :
    print("Silver catagory.")
    discount = (amount * 10)/100
    amount_payable = amount - discount
    print(f"Amount payable is {amount_payable}")

else :
    print("Bronze catagory.")
    discount = (amount * 5)/100
    amount_payable = amount - discount
    print(f"Amount payable is {amount_payable}")