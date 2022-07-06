import sys

var = 1
if len(sys.argv) == 1:
    print("error 0 arg")
else:
    print(sys.argv[-1])

