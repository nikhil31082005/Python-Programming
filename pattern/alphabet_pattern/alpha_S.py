

n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n//2+1 or i==n or (j==1 and i<=n//2+1) or (j==n and i>=n//2+1):
            print('*',end='')
        else:
            print(' ',end='')
    print()