

n = int(input())

for i in range(n+1):
    for j in range(n+1):
        if ((i==0 or i==n-1) and j<n) or ((j==0 or j==n-1) and i<n) or (i==n and j==n) or (i==n-2 and j==n-2) :
            print('*',end='')
        else :
            print(' ',end='')
    print()