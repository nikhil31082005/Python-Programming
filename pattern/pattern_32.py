


n = 5
p = 1
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(' ',end='')
    for k in range(1,p+1):
        print(k,end='')
    p = p+2
    print()