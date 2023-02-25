# 0 1 0 1 0 
# 0 0 0 0 0
# 0 1 0 1 0
# 0 0 0 0 0 
# 0 1 0 1 0 

n = 5

for i in range(1,n+1) :
    for j in range(1,n+1) :
        if j%2!=0 or (i+j)%2==0 :
            print('0',end=' ')
        else :
            print('1',end=' ')
    print()