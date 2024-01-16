'''
1.Recursion - a way of solving a problem by having a function calling itself
    - can generally be solved by iteration
    - example: Russian Doll
    - performing the same operation multiple times with different inputs
    - in every step, we try smaller inputs to make the problem smaller
    - base condition is needed to stop the recursion, otherwise infinite loop will occur

    def open_russian_doll(doll):
        if doll == 1:
            print('All dolls are opened')
        else:
            open_russian_doll(doll-1)

    1.1.why recursion:
        - recursive thinking helps break down big problems into small ones and easier to use
        - recursive code is easier to write than loops
        - used in data structures like trees and graphs

    def recursion_method(params):
        if exit from condition satisfied:
            return some value
        else:
            recursion_method(modified params)

2.                      Recursion  vs.  Iteration:
- Space efficient           No           Yes            - No stack memory require in case of iteration
- Time efficient            No           Yes            - In case of recursion system needs more time for pop and push
                                                          elements to stack memory which makes recursion less time efficient
- Easy to Code              Yes          No             - use recursion especially when we know that the problem can be
                                                          divided into similar sub problems
'''


def recursive_method_minus_one(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursive_method_minus_one(n-1)
        print(n)


def power_of_two(n):
    if n == 0:
        return 1
    else:
        power = power_of_two(n-1)
        return power*2


def power_of_two_iterative(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only'
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative or non-integer number'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def find_max_num_rec(samlpe_array, n): #O(1) + M(n-1) = M(n) Time complexity
    if n == 1:
        return samlpe_array[0]
    return max(samlpe_array[n-1], find_max_num_rec(samlpe_array, n-1))