

n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==1 :
            print('*',end='')
        elif i==n//2+1 and j<=n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()