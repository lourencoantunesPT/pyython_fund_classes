import sys

DIGIT_MAP = {
    'zero':     '0',
    'one':      '1',
    'two':      '2',
    'three':    '3',
    'four':     '4',
    'five':     '5',
    'six':      '6',
    'seven':    '7',
    'eight':    '8',
    'nine':     '9',
}


def convert(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print("conversao com sucesso! x = {x}")
    except (KeyError, TypeError):
        print("conversao falhou!!!!!! ")
    return x


# sem prints
def convert2(s):
    x = -1
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except (KeyError, TypeError):
        pass
    return x


# sem prints
def convert3(s):
    x = 0
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
    except (KeyError, TypeError) as e:
        print(f'erro de conversao: {e!r}', file=sys.stderr)
        return -1
        #raise
    return x






#>>> from  exceptional import convert

#>>> convert("three three".split())
#conversao com sucesso! x = {x}
#33

#>>> convert("three three blabla".split())
#conversao falhou!!!!!! 
#-1

#>>> convert(123)
#conversao falhou - type error
#-1
