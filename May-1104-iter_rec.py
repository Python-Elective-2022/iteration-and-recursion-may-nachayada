def iterative_power(base, exp):
    """
    base: int or float
    exp: int>=0
    returns: int or float, base^exp
    """
    value = base
    if exp==0:
        return 1
    else:
        for i in range(exp-1):
            value = value * base
        return value

def recursive_power(base, exp):
    """
    base: int or float
    exp: int >= 0
    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    elif exp > 1:
        return base * recursive_power(base, exp-1)

print(iterative_power(8, 2))
print(recursive_power(8, 2))

