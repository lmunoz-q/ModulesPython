import string


def text_analyzer(text):
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
        elif character in ("!", ",", "\'", ";", "\"", ".", "-", "?"):
            punt += 1
        elif character in " ":
            space += 1
    print(ret.format(char, upper, lower, punt, space))
