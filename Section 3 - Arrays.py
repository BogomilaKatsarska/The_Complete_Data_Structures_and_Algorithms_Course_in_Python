'''
1.Array:
    - can store data of specified type
    - elements of an array are located in a contiguous location in memory(no gap)
    - each element has unique index
    - homogenious data type
2.Types of array:
    2.1. One Dimensional: an array with a bunch of values having been declared with a single index
        - access by index: a[i]
    2.2. Multi Dimensional
        - two dimensional array a[i][j] -> a[row][column]

        - three dimensional array a[i][j][k] -> a[depth][row][column] - in the memory it is represented as 1-dimensional arr
3.Insertion to Array:
    - beginning of arr: time-consuming
'''
import array

my_array = array.array('i') #------> 0(1)
print(my_array)
my_array1 = array.array('i', [1, 2, 3, 4]) #----> O(n)
print(my_array1)
my_array1.insert(0, 6) #----> O(n) (Time); O(1)(Space); depends on the number of elements that need to be shifted right
print(my_array1)
my_array1.remove(3)  #remove by element O(1) for the last el, O(n) for all other elements time complexity
print(my_array1)


def traverse_array(array):
    for el in array: #--------> O(n)
        print(el) #-----------> O(1)


def access_element(array, index):
    if index >= len(array):
        print('Error of index')
    else:
        print(array[index])


def linear_search(arr, target): #----> O(n)
    for i in range(len(arr)-1):
        if arr[i] == target:
            return i
    return 'Error of index'


access_element([1, 2, 3], 0)
access_element([1, 2, 3], 2)
access_element([1, 2, 3], 3)


import numpy as np
np_array = np.array([], dtype=int) #------> 0(1)
print(np_array)
np_array1 = np.array([1, 2, 3, 4]) #----> O(n)
print(np_array1)

print('*'*20)
'''
One-Dimensional Array Practice
'''
from array import *

print('Step 1')
arr = array('i', [1, 2, 3, 4, 5])

for el in arr:
    print(el)

print('Step 2')
print(arr[0])

print('Step 3')
arr.append(6)
print(arr)

print('Step 4')
arr.insert(0, 11)
print(arr)

print('Step 5')
new_arr = array('i', [10, 11, 12])
arr.extend(new_arr)
print(arr)

print('Step 6')
temp_list = [21, 22, 23]
arr.fromlist(temp_list)
print(arr)

print('Step 7')
arr.remove(22)  #remove deletes the first occurance of 22 - O(n)
print(arr)

print('Step 8')
arr.pop()
print(arr)

print('Step 9')
print(f"The index of number 21 in the array is: {arr.index(21)}")

print('Step 10')
arr.reverse()
print(arr)

print('Step 11')
print(arr.buffer_info())

print('Step 12')
print('Count returns the number of occurances of sth. in the array ')
print(arr.count(11))

print('Step 13')
str_temp = arr.tostring()
print(str_temp)

print('Step 14')
print(arr[1:4]) #works exclusive last i

print('Step 15')
print(arr.tolist())

'''
Two Dimensional Array
'''
two_d_array = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]) #-----> O(m,n)
print(two_d_array)

new_two_d_array = np.insert(two_d_array, 0, [[1, 2, 3, 5]], axis=1)
print(new_two_d_array)

new_array = np.append(two_d_array, [[1, 1, 1, 1]], axis=0)
print(new_array)


def access_elements(array_to_search_in, row_index, column_index):
    if row_index >= len(array_to_search_in) or column_index >= len(array_to_search_in[0]):
        print('Incorrect index')
    else:
        print(array_to_search_in[row_index][column_index])