# # Level1 Qno 1
# age = 21
# print(age)

# # Qno 2
# item = 90.99
# print(item)

# # Qno 3
# num1 = 2
# num2 = 3
# add = num1 + num2
# sub = num1 - num2
# mul = num1 * num2
# div = num1 / num2

# print("Add: ", add)
# print("Subtract: ", sub)
# print("Multiply: ", mul)
# print("Divide: ", div)

# # Qno 4
# num1 = int(input("Enter a first number:"))
# num2 = int(input("Enter a second number:"))

# normal_div = num1 / num2

# floor_div = num1 // num2

# modulus = num1 % num2 

# print(f"Normal Division: {normal_div}")
# print(f"Floor Division: {floor_div}")
# print(f"Modulus: {modulus}")

# # Qno 5
# num_int = int(input("Enter integer value: "))
# num_float = float(input("Enter float value: "))
# result = num_float * num_int

# print(f"The result of multiplying {num_float} and {num_int} is {result}")

# Qno 6
# text = "Pragya"
# print(type(text))

# Level Qno 1
# celsius = float(input("Enter temperature in Celcius: "))
# fahrenheit = (celsius * 9/5)+ 32
# print(f"{celsius}C is equal to {fahrenheit}")

# Qno 2
# import math
# radius = float(input("Enter a radius: "))

# area = math.pi * radius ** 2

# circumference = 2 * math.pi * radius

# print(f"Area of circle: ", area)
# print(f"Circumference of circle: ", circumference)

# Qno 3
# num1 = 3
# num2 = 10
# result = abs(num1 - num2)
# print(f"The absolute difference between two numbers is: ", result)

# Qno 4
# x = round(3.14159, 2)
# print(x)

# Qno 5
# a = 10
# b = 5
# print("Two positive integer: ", a // b)

# x = -12
# y = -2
# print("Two negative integer: ", a // b )

# p = 12
# q = -2
# print("Positive and Negative integer: ", a // b)

# Level 3 Qno 1
# num = 2.2
# print("Original value: ", num)
# print("After converting", int(num))

# # Qno 2
# num_str = "25.5"
# num_float = float(num_str)
# result = num_float + 10

# print("Number in string: ", num_str)
# print("Number in float: ", num_float)
# print("After conversion: ", result)

# # Qno 3
# print(min(1,2,3))
# print(max(1,2,3))

# # Qno 4
# numbers = [5, 20, 25]
# result = sum(numbers)
# print("Sum: ", result)

# # Qno 5
# import random
# num = random.randint(1,100)
# print("Random Number: ", num)

# Level 4 Qno 1
# num = int(input("Enter a number: "))
# if (num % 2 == 0):
#     print("Even number")
# else:
#     print("Odd number")

# Qno 2
# p = float(input("Enter Principal: "))
# r = float(input("Enter Rate (%): "))
# t = float(input("Enter Time: "))
# # n = int(input("Enter the number of times is compounded per year: "))

# A = p * (1 + (r/100)) ** t

# CI = A - p

# print("Final Amount: ", round(A, 2))
# print("Result: ", round(CI, 2))

# val = int(input("Enter the seconds:  "))

# hr = int(val / (60*60))
# rem = val % (60*60)
# min = int(rem / 60)
# sec = rem % 60

# print("Hour: ", hr , " Minutes: ", min, " Seconds: ", sec)

import math
x1 = float(input("Enter x1: "))
x2 = float(input("Enter x2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))

d = math.sqrt((x2-x1)**2 + (y2-y1)**2)

print("Distance between two points: ", round(d, 3))