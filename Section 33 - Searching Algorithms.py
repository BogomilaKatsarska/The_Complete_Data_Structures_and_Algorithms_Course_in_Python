'''
1.Linear Search(sequential search)
    - Time Complexity O(N)
    - Space Complexity O(1)
2.Binary Search
    - Faster than linear search
    - Half of the remaining elements can be eliminated at a time, instead of eliminating them one by one
    - Works only for sorted arrays
'''
import math

def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


def binary_search(array, value): #Time Complexity O(1) or O(logN)
    start = 0
    end = len(array) - 1
    middle = math.floor(start + end)/2

    while not array[middle] == value and start<= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor(start + end) / 2

    if array[middle] == value:
        return middle
    else:
        return -1
