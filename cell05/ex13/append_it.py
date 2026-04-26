import sys
import re

if len(sys.argv)  != 2:
    print("none")


keyword = sys.argv[1]

count_z = keyword + 'ism'

if count_z == False:
   print('none')
else:
   print(count_z)
