

n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or (i==j and i>1 and i<=n//2+1) or (i==n+1-j and j>n//2+1 and j<n):
            print('*',end='')
        else:
            print(' ',end='')
    print()