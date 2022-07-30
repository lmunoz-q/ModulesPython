# This script has to be executed in a python console according to the subject

import string
import sys


def text_analyzer(*args):
    """
    This function counts the number of characters, upper characters, lower characters,
    punctuation characters and spaces in a given text.
    """
    if len(args) > 1:
        sys.exit("ERROR")
    elif len(args) == 0:
        text = str(input("What is the text to analyze ?\n"))
    else:
        text = args[0]
    char = len(text)
    upper = 0
    lower = 0
    punt = 0
    space = 0
    ret = "The text contains {} character(s):\n- {} upper letter(s)\n- {} lower letter(s)\n- {} punctuation mark(s)\n- {} space(s))"
    for character in text:
        if character.isupper():
            upper += 1
        elif character.islower():
            lower += 1
        elif character in string.punctuation:
            punt += 1
        elif character in string.whitespace:
            space += 1
    print(ret.format(char, upper, lower, punt, space))
