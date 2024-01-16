#1. Sum of Digits

def sum_of_digits(n):
    assert n >= 0 and int(n) == n, 'The number has to be a positive integer only'
    if n == 0:
        return 0
    else:
        return int(n % 10) + sum_of_digits(int(n//10))

#2. Power


def power(base, exponent):
    assert int(exponent) == exponent, 'The exponent must be integer number only'
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1/base * power(base, exponent+1)
    return base * power(base, exponent-1)
#3. Greatest Common Divisor
#4. Decimal to Binary