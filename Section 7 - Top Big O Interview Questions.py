def foo(array): # O(n)
    sum = 0
    product = 1

    for i in array:
        sum += i

    for i in array:
        product *= i
    print(f"Sum = {sum}, Product = {product}")


def print_pairs(array): #O(n-squared)
    for i in array:
        for j in array:
            print(f"{i}, {j}")


def print_unordered_pairs(array): #O(n-squared)
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(f'{array[i]}, {array[j]}')


def print_unordered_pairs(arr_a, arr_b): #O(ab)
    for i in range(len(arr_a)):
        for j in range(len(arr_b)):
            if arr_a[i] < arr_b[i]:
                print(f"{arr_a[i]}, {arr_b[j]}")


def print_unordered_pairs(arr_a, arr_b): #O(ab)
    for i in range(len(arr_a)):
        for j in range(len(arr_b)):
            for k in range(0, 100000):
                print(f"{arr_a[i]}, {arr_b[j]}")


def reverse(array): #O(n)
    for i in range(0, int(len(array)/2)):
        other = len(array) -i -1
        temp = array[i]
        array[other] = temp
    print(array)