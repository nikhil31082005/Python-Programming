import random

def guess(c):
    while c:
        p = c
        c -= 1
        n = int(input('Enter a number : '))
        if n == out:
            count += 1
            print("You Win")
            break
        elif n > out :
            print("Too large enter small number")
        else:
            print("Too small enter large number")
    else:
        print('You lose. better luck next time')
            


print("~~~~~~~~~~~~~~~LET'S BEGIN THE GAME~~~~~~~~~~~~~~~~")


while 100:
    choice = int(input('''
Enter 1 for easy
Enter 2 for medium
Enter 3 for hard
'''))
    out = random.randrange(1,101)
    if choice == 1:
        c = 10
        guess(c)
    elif choice == 2:
        c = 6
        guess(c)
    else:
        c = 3
        guess(c)
    k = int(input("If you want to continuee the game press 1 otherwise 0 : "))
    if k == 1:
        continue
    else:
        print("Please come again.")
        break

