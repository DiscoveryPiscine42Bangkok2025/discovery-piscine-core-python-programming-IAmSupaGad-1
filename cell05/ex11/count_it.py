import sys
x = len(sys.argv) - 1
if len(sys.argv) == 0:
   print('nope')
else:
   print('parameter ' , x)
 
   for i in range(1,len(sys.argv)):
      y = sys.argv[1]
print(y +':', len(y))

