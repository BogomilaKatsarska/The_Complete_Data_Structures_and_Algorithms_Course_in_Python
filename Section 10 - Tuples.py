'''
1.Tuple:
    - immutable sequence of Python objects(when we declare a tuple, we cannot change it)
    - comparable and hashable
    t = ('a', 'b', 'c')
    single_el_tuple = ('a',) , if the comma is not added, Python will treat it as a string
    - time complexity O(1)
    - space complexity O(n)
    - count(), index()
    - we can store tuples in a list
    - we usually use tuples for heterogeneous data types and lists for homogeneous
    - iterating through a tuple is faster than with list
'''
new_tuple = ("a", "b", "c", "d", "e")
#we use index to access elemenrs
print(new_tuple[2])
print(new_tuple[0:3])

for el in new_tuple:
    print(el)

for i in range(len(new_tuple)):
    print(new_tuple[i])

#IN operator to find if an el is in a tuple
print('a' in new_tuple)
#index() method returns the index of an el
print(new_tuple.index('c')) # If the element does not exist, it raises ValueError


def search_tuple(p_tuple, element):
    for i in range(len(p_tuple)):
        if p_tuple[i] == element:
            print(f'The element is found at {i} index')
    return 'The element is not found'

print(new_tuple + new_tuple)
print(new_tuple * 3) # create a new tuple with repetitive elements *3
print(new_tuple.count('a'))
print(new_tuple.index('a'))