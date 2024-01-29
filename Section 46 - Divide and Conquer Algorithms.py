'''
1.Properties:
    - optimal structure
    1.1. Examples:
        - Merge Sort
        - Quick Sort
'''


def fibonacci(n):
    if n < 1:
        return 'The value must be equal to or grater than 1'
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

'''
Number Factor: given N, find the ways to express N as a sum of 1, 3 and 4
'''


def number_factor(n):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        subproblem1 = number_factor(n-1)
        subproblem2 = number_factor(n-3)
        subproblem3 = number_factor(n-4)
        return subproblem1 + subproblem2 + subproblem3

print(number_factor(5))