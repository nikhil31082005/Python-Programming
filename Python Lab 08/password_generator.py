import random

ls = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890~!@#$%^&*()'

password_length = int(input("Enter the length of password : "))
for i in range(password_length):
    password = random.choice(ls)
    print(password,end='')
