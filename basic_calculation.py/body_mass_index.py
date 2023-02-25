weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in cms : "))

Height_in_metres = height/100

body_mass_index = weight / Height_in_metres ** 2

print(f"Body mass in is {body_mass_index}")