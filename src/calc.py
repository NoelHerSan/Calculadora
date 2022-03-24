import re

message_error = "Check the inputs, should be numbers or with fraction format"


# This function is check if a input value can convert to float format
def isnoterror(valor):
    """
    Validate if the input value can convert to float format.

    Args:
      valor: The parameter that can are a string with fraction format or a number

    Returns: Boolean, True if the input value can convert to float format,
                      False if the input value can not convert to float format

    """
    try:
        float(valor)
        return True
    except ValueError:
        return False


# Function that convert the input value in fraction format to float format.
def get_fractions(valor):
    """
    Convert a fraction or numeric format to float format

    Args:
      valor: in numeric format or in fraction format ('a/b')

    Returns: the input value as float number

    """
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
    """
    Calculate the sum between a and b

    Args:
      a: The first sumand
      b: The second sumand

    Returns: the sum of the elements

    """
    if isinstance(a, float) and isinstance(b, float):
        return a + b
    else:
        sum_a = get_fractions(a)
        sum_b = get_fractions(b)
        if isinstance(sum_a, float) and isinstance(sum_b, float):
            return sum_a + sum_b


# multiplication function
def calc_multiplication(a,
                        b):
    """
    Calculate the multiplication between a and b

    Args:
      a: The multiplier
      b: The multiplying

    Returns: the multiplication of the elements

    """
    if isinstance(a, float) and isinstance(b, float):
        return a * b
    else:
        multiplier = get_fractions(a)
        multiplying = get_fractions(b)
        if isinstance(multiplier, float) and isinstance(multiplying, float):
            return multiplier * multiplying
        else:
            return message_error
