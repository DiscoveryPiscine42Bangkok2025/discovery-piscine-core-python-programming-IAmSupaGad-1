import sys
x = sys.argv[1:]
if len(sys.argv)  < 3:
    print("none")
else:
    for x in reversed(x):
      print(x)

