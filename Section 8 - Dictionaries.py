'''
1. Dictionary:
    - unordered, changeable and indexed collection

2. Operations / Built-in Functions:
    - IN / NOT IN - works with the keys
    print(3 in my_dict) -> True/False
    print(3 in my_dict.values()) -> True/False - works with the values of the dict
    - LEN () - takes each KVP as a single element
    - ALL()
    print(all(my_dict)) - T/F - all keys are T
    - ANY()
    - SORTED()
    print(sorted(my_dict))

3. Dictionary                      vs.          List

    unordered(ordered as of Python 3.7)         ordered
    access via keys                             access via index
    collection of KVP                           collection of elements
    preferred when you have unique K-V          preferred when you have ordered data
    no duplicate members                        allows duplicate members


4. Dictionary Comprehension
    new_dict = {new_key:new_value for (key, value) in dict.items() if condition}

    import random
    city_names = ["Paris", "London", "Rome", "Berlin", "Madrid"]
    city_temps = {city: random.randint(10, 20) for city in city_names}
    above_25 = {city: temp for (city, temp) in city_temps.items() if temp > 25}
'''

my_dict = { #O(n)
    "Miller": "a person who owns or works in a corn mill",
    "Programmer": "a person who writes computer programs"
}

print(my_dict["Miller"])

eng_sp = dict(one='uno', two='dos', three='tres') #O(n)

my_second_dict = {'name': 'Bogomila', 'age': 28}
my_second_dict['name'] = 'Bogi' #O(1)
my_second_dict['city'] = 'Sofia'

print(my_second_dict)


def traverse_dict(dict): #O(n)
    for key in dict:
        print(key, dict[key])

traverse_dict(my_second_dict)


def search_dict(dict, value):
    for key in dict: #O(n)
        if dict[key] == value:
            return key, value
    return 'The value does not exist'

#DELETING
del my_second_dict['age'] #O(1) involves hash table
print(my_second_dict)
removed_element = my_second_dict.pop('city', None) # we can add second param in case the searched key is not found in the dict
print(removed_element)
print(my_second_dict)

my_dict.popitem() # removes the last element in the dict
my_dict.clear() #empties the dict O(n)

#ALL OTHER METHODS
newest_dict = my_second_dict.copy()
print(newest_dict)

fromkeys_dict = {}.fromkeys([1, 2, 3], 0)
print(fromkeys_dict)

# GET returns NONE if second param not added, else - returns the second provided param if the key does not exist in the dict

print(newest_dict.get('age', 27))
print(newest_dict.get('name', 'Milica'))

#dictionary.items()
print(newest_dict.items())

#keys()
print(newest_dict.keys())

#popitem() - removes and returns an arbitrary item from the dict
print(newest_dict.popitem())

#setdefault() returns the value of the key if the key is in the dict, else, inserts the key in the dict

#values() - returns list which contains values

#update()