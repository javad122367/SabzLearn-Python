# 1
print("\n","task 1: Defining the variable and assigning it a value and updating the value \n")
x = 1
y = 2
print(x := 2 , y := 4 , "\n")

# 2
print("task 2: Calculate the length and width of the rectangle \n")
rectangel_Length = input("Please set Length:  ")
rectangel_Width = input("Please set Width:   ")
print("The area of ​​the Rectangle is equal to:  " , float(rectangel_Length) * float(rectangel_Width), "\n")

# 3
print("task 3: Convert temperature from Celsius to Fahrenheit \n")
Celsius = input("Please write the temperature in Celsius:   " )
Fahrenheit = (1.8 * float(Celsius)) + 32
print("The temperature in Fahrenheit is equal to:  " , Fahrenheit , "\n")

# 4
print("task 4: Calculate the circumference and area of ​​a circle \n")
circle_Radius = input("Please enter the radius of the circle:   " )
circumference_Circle = (float(circle_Radius)*float(circle_Radius)) * 3.14
area_Circle = (float(circle_Radius)+float(circle_Radius)) * 3.14
print("The circumference of a circle is equal to:  " , circumference_Circle , "\n")
print("The area of ​​the circle is equal to:  " , area_Circle , "\n")

# 5
print("task 5: Calculate Total - Subtraction - Multiplication - Power \n")
a = input("Please enter a Number:   " )
b = input("Please enter a Number too:   " )
math_Total = float(a) + float(b) 
math_Subtraction = float(a) - float(b)
math_Multiplication = float(a) * float(b)
math_Power = float(a) ** float(b)
print(f"Total {a} and {b} :  " , math_Total , "\n"
      f"Difference {a} and {b} :  " , math_Subtraction , "\n"
      f"{a} Multiplied by {b} :  " , math_Multiplication , "\n"
      f"{a} to the power of {b} :  " , math_Power , "\n" )


# 6
print("task 6: Calculate the average of 3 numbers \n")
c = input("Please enter a First Number :   " )
d = input("Please enter a Second Number :   " )
e = input("Please enter a third Number :   " )
math_average = (float(c) + float(d) + float(e)) / 3 
print(f"Average numbers of {c} - {d} - {e} :   " , math_average , "\n")


# 7
print("task 7: Calculate the area of ​​the triangle \n")
f = input("Please enter the size of triangle base :   " )
g = input("Please enter the size of triangle height :   " )
print(f"The area of ​​the Triangle is equal to :   " , (float(f) * float(g)) / 2  , "\n")


# 8 
import datetime
now = datetime.datetime.now()
age = int(input("How old are you ?   "))
in_year = int(now.year)
print("The year in which you will be 100 years old is :  " , (in_year - age) + 100 , "\n")