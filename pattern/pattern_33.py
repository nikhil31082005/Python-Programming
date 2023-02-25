


n = 5
p = 1

for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(' ',end='')
    for k in range(p,0,-1):
        print(p,end='')
    p = p+2 
    print()