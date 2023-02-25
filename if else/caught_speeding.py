speed = int(input("Enter the speed of bike : "))
birthday = input("Today is your birthday or not. Enter 'Y' for yes and 'N' for no : ")

if birthday=='Y':
    if speed <= 65 :
        print('0')
    elif speed > 65 and speed <= 85 :
        print('1')
    else :
        print('2')

else :
    if speed <= 60 :
        print('0')
    elif speed > 60 and speed <= 80 :
        print('1')
    else :
        print('2')