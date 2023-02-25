a = int(input("Enter the number of cigars : "))
b = input("Enter 1 for true and 0 for false : ")

if b==1 :
    if a>=40  :
        print('True')
    else :
        print('False')

else :
    if a>=40 and a<=60 :
        print('True')
    else :
        print('False')