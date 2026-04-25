#!/usr/bin/env python3
import numpy as np
number = np.array([2, 8, 9, 48, 8, 22, -12, 2])
unique_greater = np.unique(number)
greater = unique_greater[unique_greater > 5]
print(number)
print(greater + 2)

