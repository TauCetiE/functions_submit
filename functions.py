import math

# Function 1: Calculate and return the area of a circle (Pi * r^2)
def area_of_circle(pi, radius):
    return pi * radius ** 2

# Function 2: Calculate and return the total due (money + money * tax)
def total_due(money, tax):
    return money + (money * tax)

# Function 3: Convert Fahrenheit to Celsius and return the result
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

# ----- Area of a Circle -----
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(math.pi, radius)
print("Area of the circle:", round(area, 2))

# ----- Taxes -----
money = float(input("Enter the amount of money: "))
tax_rate = float(input("Enter the tax rate (percent): "))
total = total_due(money, tax_rate / 100)
print("Total due:", f"{total:.2f}")

# ----- Temperature -----
fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("Temperature in Celsius:", f"{celsius:.6g}")

input("\nPress Enter to exit...")