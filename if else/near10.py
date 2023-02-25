a = int(input("Enter a number : "))
out = a%10
if a<10 :
    if a== 8 or a==9 :
        print("Near ten")
    else :
        print("Not near ten")
    
elif out==0 or out == 1 or out==2 or out==8 or out==9 :
    print('Near ten')

else :
    print('not near ten')