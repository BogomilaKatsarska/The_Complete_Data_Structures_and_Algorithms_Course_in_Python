'''
1. What is Big O: the language and the metric we use to describe the efficiency of algorithms
    - Time Complexity: a way of showing how the runtime of a function increases as the size of input increases
        we measure the number of operations
    - Space Complexity: the amount of memory that some code uses
    1.1. Omega - best case
    1.2. Theta - average case
    1.3. Omicron(Big O) - worst case

    |1|2|3|4|5|6|7|8| example: loop through an array (take 1, take 4, take 8)

2. Common Runtime Complexities:
    - 0(1) - Constant - a simple add numbers function
    - 0(N) - Linear - loop through numbers from 1 to n
    - 0(LogN) - Logarithmic - find an element in sorted array
    - O(N squared) - Quadratic - nested loops
    - O(2 to the power of n) - Exponential - double reesursion in Fibonacci

3. Space complexity: how much memory in worst case is needed at any point of the algorithm

4.Quiz: What is the complexity for the following Python code snipset?
    - sum = 0
      for i in range(n):
        sum += i ---> O(n)
    - sum = 0
      for i in range(n):
        for j in range(n):
            sum += i * j  ---> O(n^2)
    - sum = 0
      i = 1
      while i <=1:
        sum += i
        i *= 2  -----> O(logn)
    - sum = 0
      for i in range(n):
        for j in range(m):
            sum += i * j ----> O(m*n)
'''

# Constant Complexity(= Runtime Complexity): example: take the first card
def multiply_numbers(n):
    return n*n  #we always have 1 number of operation

print(multiply_numbers(2))

# Linear Complexity - time complexity will grow in direct proportion to the size of the input data
# Example: select a specific card from cards
# Drop constants: n+n = 2n time complexity => drop constant and write O(n)
def print_items(n):
    for i in range(n):
        print(i)

print(print_items(4))
# Logarithmic Complexity
# |1|2|3|4|5|6|7|8| --> |1|2|3|4| --> |1|2| --> |1| --> divide and conquer technique (two to the power of 3 = 8 => log 2 8 = 3)
# more efficient than O(n) and O(N squared) complexity

# Quadratic Complexity
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


# Space complexity
def sum(n):
    if n <= 0:
        return 0
    return n + sum(n-1) #O(n) space complexity

#How to make above to O(1) space complexity?:
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total


def pair_sum(a, b):
    return a+b


def find_biggest_number(sample_array): #Total time complexity here is O(n)
    biggest_number = sample_array[0] # ----------------> O(n)
    for i in range(1, len(sample_array)): # ------------> O(1)
        if sample_array[i] > biggest_number: # ----------> O(1)
            biggest_number = sample_array[i] # ------------> O(1)
    print(biggest_number) # ---------------------------------> O(1)
