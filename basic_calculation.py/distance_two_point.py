x1 = int(input("Enter the x coordinate of first point : "))
y1 = int(input("Enter the y coordinate of first point : "))
x2 = int(input("Enter the x coordinate of second point : "))
y2 = int(input("Enter the y coordinate of second point : "))

distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(f'The distance between points ({x1},{y1}) and ({x2},{y2}) is {distance}')