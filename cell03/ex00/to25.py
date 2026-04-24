#!/usr/bin/env python3
print("Enter a number less than 25")
x = int(input())
if x > 25:
   print("ERROR")
else:
   while x < 26:
      print("Inside the loop, my variable is " + str(x))
      x += 1


