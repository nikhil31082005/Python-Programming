import random

print("-----THANK YOU FOR CHOOSING ROCK,PAPER,SCISSOR GAME-----")

while True:
    print("DO YOU WANT TO PLAY WITH COMPUTER OR HUMAN.")
    opt = input()
    if opt == 'computer':
        choices = ['rock','paper','scissor']
        computer_choice = random.choice(choices)
        user_choice = input('Enter your choice : ')
        user_choice.lower()

        if user_choice == 'rock' and computer_choice == 'scissor' or user_choice == 'paper' and \
            computer_choice == 'rock' or user_choice == 'scissor' and computer_choice == 'paper':
            print('Your choice is',user_choice)
            print("Computer's choice is",computer_choice)
            print("HURRAY,YOU WON.")

        elif user_choice == computer_choice:
            print('Your choice is',user_choice)
            print("Computer's choice is",computer_choice)
            print("MATCH IS DRAW.")

        else :
            print('Your choice is',user_choice)
            print("Computer's choice is",computer_choice)
            print("OH NO! YOU LOSE.")

        print('DO YOU WANT TO PLAY THIS GAME ONE MORE TIME.')
        print("IF YES :ENTER 'YES' OTHERWISE 'NO")
        response = input()
        response.lower()
        if response == 'yes':
            continue
        else:
            break

    else:
        user1_choice = input('Enter user 1 choice : ')
        user2_choice = input('Enter user 2 choice : ')
        user1_choice.lower()
        user2_choice.lower()

        if user1_choice == 'rock' and user2_choice == 'scissor' or user1_choice == 'paper' and \
            user2_choice == 'rock' or user1_choice == 'scissor' and user2_choice == 'paper':
            print('User 1 choice is',user1_choice)
            print("User 2 choice is",user2_choice)
            print("HURRAY,USER 1 WON.")

        elif user1_choice == user2_choice:
            print('User 1 choice is',user1_choice)
            print("User 2 choice is",user2_choice)
            print("MATCH IS DRAW.")

        else :
            print('User 1 choice is',user1_choice)
            print("User 2 choice is",user2_choice)
            print("HURRAY,USER 2 WON.")

        print('DO YOU WANT TO PLAY THIS GAME ONE MORE TIME.')
        print("IF YES :ENTER 'YES' OTHERWISE 'NO")
        response = input()
        response.lower()
        if response == 'yes':
            continue
        else:
            break

print('Thank you for playing.')