import numpy as np


def missing_number_my_solution(arr, n):
    for i in range(0, n-1):
        if arr[i] != (i+1):
            print(arr[i]-1)
            break
        else:
            continue


missing_number_my_solution([1, 2, 3, 4, 6], 6)
missing_number_my_solution([1, 2, 3, 4, 5, 6, 8, 9], 9)


def missing_number_author_solution(arr, n):
    total = n * (n+1) // 2
    sum_arr = sum(arr)
    missing = total - sum_arr
    print(missing)


missing_number_author_solution([1, 2, 3, 4, 6], 6)
missing_number_author_solution([1, 2, 3, 4, 5, 6, 8, 9], 9)


def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print(i, j)

find_pairs([1, 2, 3, 4, 5, 6], 6)


my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def find_number(array, number):
    for i in range(len(array)):
        if array[i] == number:
            print(i)


find_number(my_array, 4)
find_number(my_array, 13)


def max_product(arr):
    arr.sort(reverse=True)
    print(arr[0]*arr[1])

max_product([1, 2, 3, 4, 5])


def middle(arr):
    arr.pop(0)
    arr.pop()
    # Option 2: return list[1:-1]
    print(arr)

middle([4, 3, 1, 4, 6, 7])

def sum_diagonal_elements(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]

    print(total)

def first_second(my_list):
    max_one = int()
    max_two = int()

    for num in my_list:
        if num > max_one:
            max_two = max_one
            max_one = num
        elif num > max_two and num != max_one:
            max_two = num
    print(f"{max_one}, {max_two}")

first_second([4, 3, 1, 4, 6, 7, 7])


def remove_duplicates(list):
    unique_list = []
    seen = set()
    for item in list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append((f"{arr[i]}+{arr[j]}"))
    return result


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def premutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False

#TODO: try below rotation again #75.
def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()