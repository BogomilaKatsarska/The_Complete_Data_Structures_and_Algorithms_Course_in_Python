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
