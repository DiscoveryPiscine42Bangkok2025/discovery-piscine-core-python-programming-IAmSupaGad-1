#!/usr/bin/env python3
x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = x*y
print(str(x) + " x "  + str(y) + " = " + str(z))
if z > 0:
   print("The result is positive")
elif z == 0:
   print("The result is positive and negative")
else:
   print("The result is negative")
