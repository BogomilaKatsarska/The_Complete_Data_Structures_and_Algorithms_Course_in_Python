#TODO: do the tasks again
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent-1)


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)


def product_of_array(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * product_of_array(arr[1:])


def recursive_range(num):
    if num <= 0:
        return 0
    return num + recursive_range(num - 1)


def fib(num):
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


def reverse(string):
    if len(string) <= 1:
        return string
    return string[len(string)-1] + reverse(string[0:len(string) - 1])


def is_palindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return is_palindrome(string[1:-1])


def some_recursive(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return some_recursive(arr[1:], cb)
    return True


def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True


def flatten(arr):
    result_arr = []
    for custom_item in arr:
        if type(custom_item) is list:
            result_arr.extend(flatten(custom_item))
        else:
            result_arr.append(custom_item)
    return result_arr


def capitalize_first(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalize_first(arr[1:])


def nested_even_sum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nested_even_sum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum


def capitalize_words(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalize_words(arr[1:])


def stringify_numbers(obj):
    new_obj = obj
    for key in new_obj:
        if type(new_obj[key]) is int:
            new_obj[key] = str(new_obj[key])
        if type(new_obj[key]) is dict:
            new_obj[key] = stringify_numbers(new_obj[key])
    return new_obj


def collect_strings(obj):
    result_arr = []
    for key in obj:
        if type(obj[key]) is str:
            result_arr.append(obj[key])
        if type(obj[key]) is dict:
            result_arr = result_arr + collect_strings(obj[key])
    return result_arr

