import sys
import re

if len(sys.argv)  != 2:
    print("none")

keyword = sys.argv[1]

count_z = keyword.count('z')

if count_z == 0:
   print('none')
else:
   print('z' * count_z)
