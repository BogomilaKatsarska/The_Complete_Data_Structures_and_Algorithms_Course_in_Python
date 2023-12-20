'''
1. [Lists]:
    - data structure that holds an ordered collection of items
    - elements don't have to be of the same type(unlike arrays)
    - mutable i.e. can change elements

2. Operators/ions:
    - 'in' - bool
    - minus index
    - insert(), append(), extend()
    - pop(), delete(), remove()
    - len(), max(), min(), sum()
    - "+" operator
    a = [1, 2]
    b = [3, 4]
    c = a + b # [1, 2, 3, 4]
    - "*" operator - repetitive el
    a = [0]
    print(a * 4) # [0, 0, 0, 0]

3. Lists and Strings:
    a = 'span'
    b = list(a)
    c = 'spam spam spam'.split()
    d = 'spam-spam-spam'.split('-')
    ('-').join(['ala', 'bala', 'nica'])

4. Lists vs Arrays:
    - On arrays you can perform arithmetic operations, while with list we receive error
    - In arrays all elements have to be of the same type, while in list you can have many different

5. List Comprehension:
    prev_list = [1, 2, 3]
    new_list = []
    for el in prev_list:
        multiply_2 = el* 2
        new_list.append(muliply_2)

    => new_list = [el*2 for el in prev_list]

    language = 'Python'
    python_list = [letter for letter in language]

    first_list = [-1, 0, -6, 3, 4, 5, 6, -18, -29]
    new_list = [el for el in first_list if el > 0]
    new_list_2 = [number if number > 0 else 0 for number in first_list]

    sentence = 'My name is Bogomila'

    def is_consonant(letter):
        vowels = 'aeiou'
        return letter.isalpha() and letter.lower() not in vowels

    consonants = [i for i in sentence if is_consonant(i)]
    print(consonants)
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

'''
Practice One Test
'''
print('Practice One Test')
# 1. What will be the output of the following code block?

arr = [[1, 2, 3, 4],
       [4, 5, 6, 7],
       [8, 9, 10, 11],
       [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())
# 4 7 11 15

# 2. What will be the output of the following code block?


def f(i, values = []):
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)
# [1] [2] [3]

# 3. What will be the output of the following code block?

arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end = " ")
# 2 3 4 5 6 6

#4. What will be the output of the following code block?

a=[1,2,3,4,5]
print(a[3:0:-1])

#[4, 3, 2]

#5. What will be the output of the following code block?

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)
#22

#6. What is the correct command to shuffle the following list?

fruit=['apple', 'banana', 'papaya', 'cherry']

#random.shuffle(fruit)

#8. What will be the output of the following code snippet?

def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])
#3 44

#9. What will be the output of the following code block?

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]


def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element:
                v = element

    return v


print(fun(data[0]))
#4

#10. What will be the output of the following code block?
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[::2] = 10, 20, 30, 40, 50, 60
print(a)
# ValueError: attempt to assign sequence of size 6 to extended slice of size 5