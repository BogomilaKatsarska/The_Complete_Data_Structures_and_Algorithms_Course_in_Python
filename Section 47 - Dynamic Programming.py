'''
1.What is Dynamic Programming(Overlapping Property):
    - Algorithmic technique for solving an optimization problem by breaking it down to simpler subproblems and utilizing
    the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems
    - Optimal Substructure
    - Overlapping Subproblem

    #TOP DOWN WITH MEMOIZATION
    #BOTTOM UP WITH TABULATION
'''

def fib_memoization(n, memo):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n not in memo:
        memo[n] = fib_memoization(n-1, memo) + fib_memoization(n-2, memo)
    return memo[n]

my_dict = {}
print(fib_memoization(6, my_dict))


def fib_tabulation(n):
    tb = [0, 1]
    for i in range(2, n+1):
        tb.append(tb[i-1] + tb[i-2])
    return tb[n-1]

print(fib_tabulation(6))


def num_factor_topdown(n, temp_dict):
    if n in (0, 1, 2):
        return 1
    elif n == 3:
        return 2
    else:
        if n not in temp_dict:
            subproblem1 = num_factor_topdown(n-1, temp_dict)
            subproblem2 = num_factor_topdown(n - 3, temp_dict)
            subproblem3 = num_factor_topdown(n - 4, temp_dict)
            temp_dict[n] = subproblem1 + subproblem2 + subproblem3
        return temp_dict[n]

print(num_factor_topdown(5, {}))


def num_factor_bottomup(n):
    temp_arr = [1, 1, 1, 2]
    for i in range(4, n+1):
        temp_arr.append(temp_arr[i-1] + temp_arr[i-3] + temp_arr[i-4])
    return temp_arr[n]

print(num_factor_bottomup(5))


def house_robber_TD(houses, curr_index, temp_dict):
    if curr_index >= len(houses):
        return 0
    else:
        if curr_index not in temp_dict:
            steal_fist_house = houses[curr_index] + house_robber_TD(houses, curr_index+2, temp_dict)
            skip_first_house = house_robber_TD(houses, curr_index+1, temp_dict)
            temp_dict[curr_index] = max(steal_fist_house, skip_first_house)
        return temp_dict[curr_index]


houses = [6, 7, 1, 30, 8, 2, 4]
print(house_robber_TD(houses, 0, {}))

def house_robber_BU(houses, curr_index):
    temp_arr = [0] * (len(houses) +2)
    for i in range(len(houses)-1, -1, -1):
        temp_arr[i] = max(houses[i] + temp_arr[i+2], temp_arr[i+1])
    return temp_arr[0]

print(house_robber_BU(houses, 0))


def findMinOperationBU(s1, s2, tempDict):
    for i1 in range(len(s1) + 1):
        dictKey = str(i1) + '0'
        tempDict[dictKey] = i1
    for i2 in range(len(s2) + 1):
        dictKey = '0' + str(i2)
        tempDict[dictKey] = i2

    for i1 in range(1, len(s1) + 1):
        for i2 in range(1, len(s2) + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                dictKey = str(i1) + str(i2)
                dictKey1 = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = tempDict[dictKey1]
            else:
                dictKey = str(i1) + str(i2)
                dictKeyD = str(i1 - 1) + str(i2)
                dictKeyI = str(i1) + str(i2 - 1)
                dictKeyR = str(i1 - 1) + str(i2 - 1)
                tempDict[dictKey] = 1 + min(tempDict[dictKeyD], min(tempDict[dictKeyI], tempDict[dictKeyR]))

    dictKey = str(len(s1)) + str(len(s2))
    return tempDict[dictKey]

'''
zero one knapsack problem
'''
class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def zoKnapsack(items, capacity, currentIndex, tempDict):
    dictKey = str(currentIndex) + str(capacity)
    if capacity <= 0 or currentIndex < 0 or currentIndex >= len(items):
        return 0
    elif dictKey in tempDict:
        return tempDict[currentIndex]
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zoKnapsack(items, capacity - items[currentIndex].weight,
                                                          currentIndex + 1, tempDict)
        profit2 = zoKnapsack(items, capacity, currentIndex + 1, tempDict)
        tempDict[dictKey] = max(profit1, profit2)
        return tempDict[dictKey]
    else:
        return 0


def zoKnapsackBU(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0
    numberOfRows = len(profits) + 1
    dp = [[None for i in range(capacity+2)] for j in range(numberOfRows)]
    for i in range(numberOfRows):
        dp[i][0] = 0
    for i in range(capacity+1):
        dp[numberOfRows-1][i] = 0
    for row in range(numberOfRows-2, -1, -1):
        for column in range(1,capacity+1):
            profit1 = 0
            profit2 = 0
            if weights[row] <= column:
                profit1 = profits[row] + dp[row + 1][column - weights[row]]
            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][capacity]
