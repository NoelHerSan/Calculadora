import re

message_error = "Check the inputs, should be only numbers or with fraction format"


# This function is needed for check if a input value can convert to float format
def isnoterror(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


# Function that convert the input value in fraction format to float format.
def get_fractions(valor):
    mystring = str(valor)
    verifyfraction = re.search(r"(?:[1-9][0-9]*|0)\/[1-9][0-9]*", mystring)
    if verifyfraction:
        split_string = valor.split('/')
        decimal = int(split_string[0]) / int(split_string[1])
        return decimal
    elif isnoterror(valor):
        return float(valor)
    else:
        return 0
        
# Sum function
def calc_sum(a,
             b):
    if isinstance(a, float) and isinstance(b, float):
        return a + b
    else:
        sum_a = get_fractions(a)
        sum_b = get_fractions(b)
        if isinstance(sum_a, float) and isinstance(sum_b, float):
            return sum_a + sum_b
        else:
            return message_error