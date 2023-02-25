L = float(input("Enter the length of floor :\n"))
B = float(input("Enter the breadth of floor :\n"))

l = float(input("Enter the length of tile :\n"))
b = float(input("Enter the breadth of tile :\n"))

AREA = L*B
area = l*b

tiles = -(-AREA//area)

print("No of tiles :",tiles)