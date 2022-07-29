import sys

var = 1
if len(sys.argv) == 1:
    print("ya un truc a faire la")
else:
    for arguments in sys.argv:
        print(arguments)