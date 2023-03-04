n = int(input("Enter the rows size : "))

c = input("Enter an alphabet : ")

if c=='A' or c=='a':
    for i in range(n):
        for j in range(1,n):
            if i==0 or j == n-1 or i==n//2 or j == 1 :
                print("*",end=' ')
            else :
                print(' ',end=' ')
        print()

elif c=='B' or c=='b':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or (i==1 and j<n) or (i==n and j<n) or (j==n and i>1 and i<n) or i==n//2+1:
               print("*",end=' ')
            else:
                print(" ",end=' ')
        print()

elif c=='C' or c=='c':
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0:
                print("*",end=' ')
            else:
               print(' ',end=' ')
        print()

elif c=='D' or c=='d':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or (i==1 or i==n) and j<=n-1:
                print('*',end='')
            elif i!=1 and i!=n and j == n:
                print('*',end='')
            else:
                print(' ',end='')
        print()

elif c=='E' or c=='e':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n//2+1 or i==n or j==1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='F' or c=='f':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or i==1 :
                print('*',end=' ')
            elif i==n//2+1 and j<=n-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='G' or c=='g':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i==1 or i==n or j==1) or (j==n and i>n//2) or (i==n//2+1 and j>n//2):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='H' or c=='h':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or i==n//2+1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='I' or c=='i':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==n//2+1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='J' or c=='j':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or j==n//2+1 or (i==n and j<=n//2+1) or (j==1 and i>=n-1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='K' or c=='k':
    d = n//2+1
    for i in range(1,n+1):
        for j in range(1,n//2+2):
            if j==1 or j == d:
                print('* ',end=' ')
            else:
                print(' ',end=' ')
        if i <= n//2:
            d -= 1
        else:
            d+=1
        print()

elif c=='L' or c=='l':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or i==n:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='M' or c=='m':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or (i==j and i>1 and i<=n//2+1) or (i==n+1-j and j>n//2+1 and j<n):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='N' or c=='n':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or i==j:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='O' or c=='o':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==1 or j==n:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='P' or c=='p':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or (i==1 and j<=n//2+1) or (i==n//2+1 and j<=n//2+1) or (j==n//2+1 and i<=n//2+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='Q' or c=='q':
    for i in range(n+1):
        for j in range(n+1):
            if ((i==0 or i==n-1) and j<n) or ((j==0 or j==n-1) and i<n) or (i==n and j==n) or (i==n-2 and j==n-2) :
                print('*',end=' ')
            else :
                print(' ',end=' ')
        print()

elif c=='R' or c=='r':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or ((i==1 or i==n//2+1) and j<=n//2+1) or (j==n//2+1 and i<=n//2) or (i==j+n//2 and i>n//2):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='S' or c=='s':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n//2+1 or i==n or (j==1 and i<=n//2+1) or (j==n and i>=n//2+1):
                print('*',end='')
            else:
                print(' ',end='')
        print()

elif c=='T' or c=='t':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or j==n//2+1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='U' or c=='u':
    for i  in range(1,n+1):
        for j in range(1,n+1):
            if j==1 or j==n or i==n:
                print('*',end='')
            else:
                print(' ',end='')
        print()

elif c=='V' or c=='v':
    for i in range(1,n+1):
        for j in range(1,2*n):
            if i==j or (j>n and i+j==2*n):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='W' or c=='w':
    for i in range(1,n+1):
        for  j in range(1,n+1):
            if j==1 or j==n or (i>=n//2+1 and j<=n//2+1 and j==n+1-i) or (j>=n//2+1 and i>=n//2+1 and i==j):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='X' or c=='x':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j or j==n+1-i:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='Y' or c=='y':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i==j and i<=n//2+1 and j<=n//2+1) or (j==n+1-i and j>n//2+1 and i<n//2+1) or( j==n//2+1 and i>n//2+1):
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

elif c=='Z' or c=='z':
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==n+1-i:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()

else:
    print("Enter valid character.")
