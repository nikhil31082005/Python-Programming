pizza_size = input("Enter the size of pizza :")  # small , medium , large
pizza_size = pizza_size.lower()

if pizza_size == 'small':
    s = int(input("How many small pizza you want : "))
    peporoni = input("You want to add peporoni or not : ")
    if peporoni == 'yes':
        cheez = input("You want to add some extra cheez or not : ")
        if cheez == 'yes':
            small_pizza_amount = 100*s + s*30 + s*20
        else:
            small_pizza_amount = 100*s + s*30
    else:
        cheez = input("You want to add some extra cheez or not : ")
        if cheez == 'yes':
            small_pizza_amount = 100*s + s*20
        else:
            small_pizza_amount = 100*s
    print(f'Your total amount is {small_pizza_amount} Rupee.')

elif pizza_size == 'medium':
    m = int(input("How many medium pizza you want : "))
    peporoni = input("You want to add peporoni or not : ")
    if peporoni == 'yes':
        cheez = input("You want to add some extra cheez or not : ")
        if cheez == 'yes':
            medium_pizza_amount = 200*m + m*50 + m*20
        else:
            medium_pizza_amount = 200*m + m*50
    else:
        cheez = input("You want to add some extra cheez or not : ")
        if cheez == 'yes':
            medium_pizza_amount = 200*m + m*20
        else:
            medium_pizza_amount = 200*m
    print(f'Your total amount is {medium_pizza_amount} Rupee.')

elif pizza_size == 'large':
    m = int(input("How many large pizza you want : "))
    peporoni = input("You want to add peporoni or not : ")
    if peporoni == 'yes':
        cheez = input("You want to add some extra cheez or not : ")
        if cheez == 'yes':
            large_pizza_amount = 300*m + m*30 + m*20
        else:
            large_pizza_amount = 300*m + m*30
    else:
        cheez = input("You want to add some extra cheez or not : ")
        if cheez == 'yes':
            large_pizza_amount = 300*m + m*20
        else:
            large_pizza_amount = 300*m
    print(f'Your total amount is {large_pizza_amount} Rupee.')

else :
    print("Enter the correct size of pizza.")