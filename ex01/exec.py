import sys


def swap(string):
    return string[-1:] + string[1:-1] + string[:1]


if len(sys.argv) > 1:
    print(swap(sys.argv[1:]))
