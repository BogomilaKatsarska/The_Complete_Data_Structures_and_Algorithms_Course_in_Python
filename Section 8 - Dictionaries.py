'''
1.Dictionary:
    - unordered, changeable and indexed collection
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