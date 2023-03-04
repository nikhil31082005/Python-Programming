

n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or (i==1 and j<n) or (i==n and j<n) or (j==n and i>1 and i<n) or i==n//2+1:
            print("*",end='')
        else:
            print(" ",end='')
    print()