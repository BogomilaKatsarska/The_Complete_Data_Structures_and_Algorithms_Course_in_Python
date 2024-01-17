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
'''
gcd(8, 12) = 4
8  = 2*2*2
12 = 2*2*3
=> the greatest common divisor is 2*2 as it is the common between 2 of them


Euclidean algorithm
gcd(48, 18)
Step 1 : 48/18 = 2 remainder 12
Step 2 : 18/12 = 1 remainder 6
Step 3 : 12/6  = 2 remainder 0
gcd(a, 0) = a
gcd(a, b) = gcd(b, a mod b)
'''


def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integer only!'
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#4. Decimal to Binary

def decimal_to_binary(n):
    assert int(n) == n, 'The parameter must be an integer only'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimal_to_binary(int(n/2))