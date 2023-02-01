mystr = "Harpy is a good boy"
print(len(mystr))   # Length of string
# print(mystr)   # print string

#  for positive indices
"""print(mystr[0:5])  # mystr[0] = including char , mystr[5] = excluding char
print(mystr[0:5:2])   # 2 = print first char and exclude second character and then print third character and so on
print(mystr[0:19:3])  # print first char and exclude second and third character and then print fourth char and so on
print(mystr[::])  #  print all char
print(mystr[0:19:1])   # print all char"""

#  for negative indices
print(mystr[::-1])    # Reverse the string
print(mystr[-4:])     # print four char from last
print(mystr[-4:-2])   # first take four char from last and then remove two char from four char from last and then print
print(mystr[2:4])