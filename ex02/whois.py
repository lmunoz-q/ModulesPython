import sys

if len(sys.argv) == 2 and sys.argv[1].isdigit():
    if int(sys.argv[1]) == 0:
        print("I'm Zero")
    elif int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
else:
    print("Usage : ./exe [integer]")
