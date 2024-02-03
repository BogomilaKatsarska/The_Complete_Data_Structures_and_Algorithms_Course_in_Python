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

'''
House Robber:
Given N number of houses along the street with some amount of money
Adjacent houses cannot be stollen
Find the max amount that can be stollen
'''


def house_robber(houses, current_index):
    if current_index >= len(houses):
        return 0
    else:
        steal_first_house = houses[current_index] + house_robber(houses, current_index+2)
        skip_first_house = house_robber(houses, current_index+1)
        return max(steal_first_house, skip_first_house)

houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber(houses, 0))

'''
Converting one string to another:
-S1 and S2 are given strings
- Convert S2 to S1 using delete, insert or replace
- Find the min count of edit operations
'''


def find_min_operation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return find_min_operation(s1, s2, index1+1, index2+1)
    else:
        delete_operation = 1 + find_min_operation(s1, s2, index1, index2+1)
        insert_operation = 1 + find_min_operation(s1, s2, index1+1, index2)
        replace_operation = 1 + find_min_operation(s1, s2, index1+1, index2+1)
        return min(delete_operation, insert_operation, replace_operation)

print(find_min_operation("table", "tbrles", 0, 0))

'''
Zero One Knapsack Problem:
- Given the weights and profits of N items
- Find the max profit within given capacity of C
- Items cannot be broken
'''
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def zero_one_knapsack(items, capacity, curr_index):
    if capacity <= 0 or curr_index < 0 or curr_index >= len(items):
        return 0
    elif items[curr_index].weight <= capacity:
        profit1 = items[curr_index].profit + zero_one_knapsack(items, capacity-items[curr_index].weight, curr_index+1)
        profit2 = zero_one_knapsack(items, capacity, curr_index+1)
        return max(profit1, profit2)
    else:
        return 0


mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 5)
banana = Item(72, 5)
items = [mango, orange, apple, banana]

print(zero_one_knapsack(items, 7, 0))

'''
Longest Common Subsequence Problem:
- S1 and S2 are given strings
- Find the length of the longest subsequence which is common to both strings
- subsequence: a sequence that can be driven from another sequence by deleting some elements without changing the order of them
'''

def longest_common_subsequence(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + find_min_operation(s1, s2, index1+1, index2+1)
    else:
        op1 = longest_common_subsequence(s1, s2, index1, index2+1)
        op2 = longest_common_subsequence(s1, s2, index1+1, index2)
        return max(op1, op2)

print(longest_common_subsequence('elephant', 'eretpat', 0, 0))


'''
Longest Palindromic Subsequence:
- S is a given string
- Find the longest palindromic subsequence
- Palindrome is a string that reads the same backwards as well as forwards
'''


def longest_palindromic_subsequence(s, start_index, end_index):
    if start_index > end_index:
        return 0
    elif start_index == end_index:
        return 1
    elif s[start_index] == s[end_index]:
        return 2 + longest_palindromic_subsequence(s, start_index+1, end_index-1)
    else:
        op1 = longest_palindromic_subsequence(s, start_index, end_index-1)
        op2 = longest_palindromic_subsequence(s, start_index+1, end_index)
        return max(op1, op2)


print(longest_palindromic_subsequence('ELRMENMET', 0, 8))

'''
Minimum cost to reach the last cell
- 2D Matrix is given 
- Each cell has a cost associated with it for accessing
- We need to start from (0,0) cell and go down to (n-1, n-1) cell
- We can go only to right or down cell from current cell
- Find the way in which the cost is minimum
'''

def min_cost(twoDArray, row, col):
    if row == -1 or col == -1:
        return float('inf')
    elif row == 0 and col == 0:
        return twoDArray[0][0]
    else:
        op1 = min_cost(twoDArray, row-1, col)
        op2 = min_cost(twoDArray, row, col-1)
        return twoDArray[row][col] + min(op1, op2)

twoDList = [[4,7,8,6,4],
            [6,7,3,9,2],
            [3,8,1,2,4],
            [7,1,7,3,7],
            [2,9,8,9,3]]
print(min_cost(twoDList, 4, 4))

'''
Number of paths to reach the last cell with given cost:
- 2D matrix is given
- Each cell has a cost associated with it for accessing
- We need to start from (0,0) cell and go till (n-1)(n-1) cell
- We can go only right or down cell from current cell
- We are given TC to reach the last cell
- Find the number of ways to reach end of matrix given TC
'''

def number_of_paths(twoDArray, row, col, cost):
    if cost < 0:
        return 0
    elif row == 0 and col == 0:
        if twoDArray[0][0] - cost == 0:
            return 1
        else:
            return 0
    elif row == 0:
        return number_of_paths(twoDArray, 0, col-1, cost-twoDArray[row][col])
    elif col == 0:
        return number_of_paths(twoDArray, row-1, 0, cost-twoDArray[row][col])
    else:
        op1 = number_of_paths(twoDArray, row-1, col-1, cost - twoDArray[row][col])
        op2 = number_of_paths(twoDArray, row, col-1, cost - twoDArray[row][col])
        return op1 + op2

print(number_of_paths(twoDList, 3, 3, 25))