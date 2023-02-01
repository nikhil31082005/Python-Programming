# variable
"""
var1 = "Nikhil "  # for String
var2 = 77  # for integer
var3 = 45.6  # for float
var4 = "Sikarwar"
print(var2+var3)  # add two num
print(var1 + var4)  # concatenate two Strings
print(10 * var1)  # Print Nikhil 10 times
print(10*var2)  # Multiply var2 by 10
print(10*"Hello World\n")  # Print Hello World 10 times

"""
# data type
"""
var1 = "67"  # for String
var2 = 77  # for integer
var3 = 45.6  # for float
var4 = "56"
print(type(var1))  # to find datatype of variable
print(type(var2))
print(type(var3))
"""

# Type casting
"""
var1 = "67"  # for String
var2 = 77  # for integer
var3 = 45.6  # for float
var4 = "56"
print(var1+var4)  # concatenate two Strings
print(int(var1) + int(var4))  # Convert string into integer then add them
"""


# Input From User

print("Enter the number")
var1 = input()    # taken number as string so first type cast it and change it into integer to perform arithmetic operation on it
print("your number is:", var1)
print("your number is:", 10*var1)
print("your number is:", int(var1)*10)
