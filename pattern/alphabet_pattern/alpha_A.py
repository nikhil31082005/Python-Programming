

n = int(input())

for i in range(n):
    for j in range(1,n):
        if i==0 or j == n-1 or i==n//2 or j == 1 :
            print("*",end='')
        else :
            print(' ',end='')
    print()