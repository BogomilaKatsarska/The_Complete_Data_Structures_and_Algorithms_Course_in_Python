'''
1. [Lists]:
    - data structure that holds an ordered collection of items
    - elements don't have to be of the same type(unlike arrays)
    - mutable i.e. can change elements
2. Operators:
    - 'in' - bool
    - minus index
    - insert(), append(), extend()
    - pop(), delete(), remove()

'''

integers = [1, 2, 3, 4]
string_list = ['Milk', 'Cheese', 'Butter']
mixed_list = [1, 1.4, 'spam']

for el in string_list:
    print(el)

for i in range(len(string_list)):
    string_list[i] = string_list[i] + '+'
    print(string_list)

print('Milk' in string_list)
print(string_list[-1])

string_list[2] = 'Yoghurt' #---------> O(1) T
print(string_list)
string_list.insert(0, 'Soda') #--------> O(n) T
print(string_list)
string_list.append('Bread') #--------> O(1) T
print(string_list)
string_list.extend(['Chips', 'Apples']) #--> O(n) T
print(string_list)
print(string_list[0:2])
string_list[0:2] = ['Ala', 'Bala']
print(string_list)
string_list.pop(1) #pop(1) removes the element on 1st index; keeps the deleted element in itself
print(string_list)
del string_list[1] #del is used for index deletion when we do not needed the deleted element
del mixed_list[0:2]
print(string_list)
print(mixed_list)
#remove deletes by provided value, not index
string_list.remove('Bread')
print(string_list)

def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search(string_list, 'Chips'))