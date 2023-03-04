
n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or (i==1 or i==n) and j<=n-1:
            print('*',end='')
        elif i!=1 and i!=n and j == n:
            print('*',end='')
        else:
            print(' ',end='')
    print()