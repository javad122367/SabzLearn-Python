# 1 - Calculate the circumference and area of ​​a circle
# Formula : circumference= R * R * 3.14 & area= R+R*3.14
print("1: Calculate the circumference and area of ​​a circle \n")
circle_Radius = float(input("Please enter the radius of the circle:   " ))
circle_Circumference = (circle_Radius * circle_Radius) * 3.14
circle_Area = (circle_Radius + circle_Radius) * 3.14
print("Circumference =", round(circle_Circumference , 2) ,"cm")
print("Area =", round(circle_Area , 2) ,"cm \n")


# 2 - Calculate the square and cube of a number
# Formula: square = a ** 2 & cube = a ** 3
print("2: Calculate the square and cube of a number \n")
a = float(input("Please enter the size of one side of the square:   " ))
a_Square = a ** 2
a_Cube = a ** 3
print("Square =", round(a_Square , 2) ,"cm")
print("Area =", round(a_Cube , 2) ,"cm \n")

# 3- Calculation of the first number to the power of the second number
# Formula: x = b ** c
print("3: Calculation of the first number to the power of the second number \n")
b = float(input("Enter First Number:  "))
c = float(input("Enter Second Number:  "))
print("Result: ", round(b ** c , 2) , "\n")

# 4- Calculate the average of 3 numbers
# Formula: x + y + z / 3
print("3: Calculate the average of 3 numbers \n")
d = float(input("Please enter a First Number :   " ))
e = float(input("Please enter a Second Number :   " ))
f = float(input("Please enter a third Number :   " ))
average = (d + e + f ) / 3 
print("Average:", round(average , 2), "\n")