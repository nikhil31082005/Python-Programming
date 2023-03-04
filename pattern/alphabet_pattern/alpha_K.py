

n = int(input())
d = n//2+1
for i in range(1,n+1):
    for j in range(1,n//2+2):
        if j==1 or j == d:
            print('* ',end='')
        else:
            print(' ',end='')
    if i <= n//2:
        d -= 1
    else:
        d+=1
    print()