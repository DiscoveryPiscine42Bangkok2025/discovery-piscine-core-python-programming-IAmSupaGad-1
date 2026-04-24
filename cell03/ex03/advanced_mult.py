#!/usr/bin/env python3
i = 0
while i <= 10:
    print("Table de " + str(i) + ": ", end="")
    j = 0
    while j <= 10:
        print(f"{i*j:4}", end="")
        j += 1
    print()
    i += 1