'''
1.Greedy Algorithm:
    - an algorithmic paradigm that builds the solution piece by piece
    - in each step it chooses the piece that offers most obvious and immediate benefit
    - it fits perfectly for those solution in which local optimal solutions led to global solution
    1.1.Examples:
        - insertion sort
        - topological sort
        - selection sort
        - prim algorithm
        - kruskal algorithm
'''

#Activity Selection Problem
activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9],
                 ]

def print_max_activities(activities):
    activities.sort(key=lambda x: x[2]) #sorts activities by second index
    i = 0
    first_activity = activities[i][0]
    print(first_activity)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j

print_max_activities(activities)

#Coin Change Problem
def coin_change(total_number, coins):
    n = total_number
    coins.sort()
    index = len(coins) - 1
    while True:
        coin_value = coins[index]
        if n >= coin_value:
            print(coin_value)
            n = n - coin_value
        if n < coin_value:
            index -= 1
        if n == 0:
            break

coins = [1,2,5,20,50,100]
coin_change(201, coins)


#Fractional Knapsack Problem
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight #density


def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    used_capacity = 0
    total_value = 0
    for i in items:
        if used_capacity + i.weight <= capacity:
            used_capacity += i.weight
            total_value += i.value
        else:
            unused_weight = capacity - used_capacity
            value = i.ratio * unused_weight
            used_capacity += unused_weight
            total_value += value

        if used_capacity == capacity:
            break

    print(f'Total value obtained: {str(total_value)}')


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
custom_list = [item1, item2, item3]

fractional_knapsack(custom_list, 50)