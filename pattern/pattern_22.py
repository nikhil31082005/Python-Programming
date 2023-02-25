# 1 
# 0 0
# 1 1 1 
# 0 0 0 0
# 1 1 1 1 1

n = 5
for i in range(n):
    for j in range(i+1):
        if i%2==0:
            print('1',end=' ')
        else :
            print('0',end=' ')
    print()

