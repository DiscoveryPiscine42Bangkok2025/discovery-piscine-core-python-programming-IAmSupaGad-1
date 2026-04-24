#!/usr/bin/env python3
x = str(input("What you gotta say? : "))
while True:
    i = str(input('I got that! Anything else? : '))
    if i == ("STOP"):
        break
    else:
        print(i)