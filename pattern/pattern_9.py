
# 1 1 1 2 1 3 
# 2 1 2 2 2 3
# 3 1 3 2 3 3
# 4 1 4 2 4 3
# 5 1 5 2 5 3 



n = 5

for i in range(n) :
    for j in range(n-2) :
        print(f'{i+1} {j+1}',end = ' ')
    print()