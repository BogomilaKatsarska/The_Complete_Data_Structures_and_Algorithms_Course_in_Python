'''
1.Sorting: arranging data in a particular format - ASC / DESC
2.Types of Sorting:
    2.1. Space used:
        - In place: sorting algorithms which does not require any extra space for sorting
        - Out of place: sorting algorithms which require extra space for sorting
    2.2. Stability:
        - Stable: if a sorting algorithm after sorting the content does not change the sequence
        of similar content in which they appear, then this sorting is called stable sorting
        - Unstable: if a sorting algorithm after sorting the content changes the sequence of
        similar content in which they appear, then it is called unstable sort
3.Sorting Terminologies:
    - Increasing order: if a successive element is greater than the previous one
    - Decreasing order: if a successive element is less than the previous one
    - Non-Increasing order: if a successive element is less than or equal to its previous element in
        a sequence(11, 9, 7, 5, 5, 5, 3, 1)
    - Non-Decreasing order: if a successive element is greater than or equal to its previous element in
        a sequence(1, 3, 5, 5, 5, 7, 9, 11)


'''
import math

# Bubble Sort:
#     - Also referred as sinking sort
#     - We repeatedly compare each pair of adjacent items and swap them if they are in wrong order
# When TO/NOT TO use?
#     - TO: when input is already sorted
#     - TO: when space is concern
#     - TO: easy to implement
#
#     - NOT TO: when average time complexity is concern


def bubble_sort(custom_list): # Time Complexity: O(n^2); Space Complexity: O(1)
    for i in range(len(custom_list-1)):
        for j in range(len(custom_list)-i-1):
            if custom_list[j] > custom_list[j+1]:
                custom_list[j], custom_list[j+1] = custom_list[j+1], custom_list[j]
    print(custom_list)


# Selection Sort:
#     - In case of selection sort, we repeatedly find the minimum element and move it to the sorted part
#     of array to make unsorted part sorted
# When TO/NOT TO use?
#     - TO: when we have insufficient memory
#     - TO: easy to implement
#
#     - NOT TO: time is concern

def selection_sort(custom_list):
    for i in range(len(custom_list)):
        min_index = i
        for j in range(i+1, len(custom_list)):
            if custom_list(min_index) > custom_list[j]:
                min_index = j
        custom_list[i], custom_list[min_index] = custom_list[min_index], custom_list[i]
    print(custom_list)


# Insertion Sort:
#     - Divide the given array into two parts
#     - Take first element from unsorted array and find its correct position in sorted array
#     - Repeat until unsorted array is empty
# When TO/NOT TO use?
#     - TO: when we have insufficient memory
#     - TO: easy to implement
#     - TO: when we have continuous inflow of numbers and we want to keep them sorted
#
#     - NOT TO: when time is a concern

def insertion_sort(custom_list): #Time Complexity: O(N^2); Space Complexity: O(1)
    for i in range(1, len(custom_list)):
        key = custom_list[i]
        j = i-1
        while j >= 0 and key < custom_list[j]:
            custom_list[j+1] = custom_list[j]
        custom_list[j+1] = key
    return custom_list


# Bucket Sort:
#     - Create buckets and distribute elements of array into buckets
#     - Sort buckets individually
#     - Merge buckets after sorting
#
#     Number of buckets = round(sqrt(number of elements))
#     Appropriate bucket = ceil(Value * NumOfBuckets / MaxValue)
# When TO/NOT TO use?
#     - TO: when input uniformly distributed over range
#
#     -NOT TO: when space is concern


def bucket_sort(custom_list): #Time Complexity: O(N^2); Space Complexity: O(N)
    number_of_buckets = round(math.sqrt(len(custom_list)))
    max_value = max(custom_list)
    arr = []

    for i in range(number_of_buckets):
        arr.append([])
    for j in custom_list:
        index_b = math.ceil(j*number_of_buckets/max_value)
        arr[index_b-1].append(j)
    for i in range(number_of_buckets):
        arr[i] = insertion_sort(arr[i])

    k = 0
    for i in range(number_of_buckets):
        for j in range(len(arr[i])):
            custom_list[k] = arr[i][j]
            k += 1
    return custom_list


def bucket_sort_negative(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets

    buckets = [[] for _ in range(numberofBuckets)]

    for j in customList:
        if j == maxValue:
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)

    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertion_sort(buckets[i])
        sorted_array.extend(buckets[i])

    return sorted_array

# Merge Sort
#     - Merger sort is a divide and conquer algorithm
#     - Divide the input array in two halves and we keep halving recursively until they become too small that
#         cannot be broken further
#     - Merge halves by sorting them
# When TO/NOT TO use?
#     - TO: when you need stable sort
#     - TO: when average expected time is O(NlogN)
#
#     - NOT TO: when space is concern

#MERGE SORT
def merge(custom_list, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = custom_list[l+i]

    for j in range(0, n2):
        R[j] = custom_list[m+1+j]

    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            custom_list[k] = L[i]
        else:
            custom_list[k] = R[j]
        k += 1
    while i < n2:
        custom_list[k] = R[j]
        j += 1
        k += 1


def merge_sort(custom_list, l, r):
    if l < r:
        m = (l + (r-1)) // 2
        merge_sort(custom_list, l, m)
        merge_sort(custom_list, m+1, r)
        merge(custom_list, l, m, r)
    return custom_list



#PIVOT + QUICK SORT
def swap(my_list, index1, index2):
    # temp = my_list[index1]
    # my_list[index1] = my_list[index2]
    # my_list[index2] = temp
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort_helper(my_list, left_index, right_index):
    if left_index < right_index:
        pivot_index = pivot(my_list, left_index, right_index)
        quick_sort_helper(my_list, left_index, pivot_index-1)
        quick_sort_helper(my_list, pivot_index+1, right_index)
    return my_list


def quick_sort(my_list):
    return quick_sort_helper(my_list, 0, len(my_list)-1)

'''
Heap Sort:
    - Insert Data into Binary Heap Tree
    - Extract Data from Binary Heap Tree
    - It is best suited with array, it does not work with linked list
'''


def heapify(custom_list, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and custom_list[l] < custom_list[smallest]:
        smallest = l

    if r < n and custom_list[r] < custom_list[smallest]:
        smallest = r

    if smallest != i:
        custom_list[i], custom_list[smallest] = custom_list[smallest], custom_list[i]
        heapify(custom_list, n, smallest)


def heap_sort(custom_list):
    n = len(custom_list)
    for i in range(int(n/2)-1, -1, -1):
        heapify(custom_list, n, i)

    for i in range(n-1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapify(custom_list, i, 0)
    custom_list.reversed()
