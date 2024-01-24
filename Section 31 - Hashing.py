'''
1.Hash Functions
    - Hashing: a method of sorting and indexing data. The idea behind hashing is to allow large amounts of data to be
    indexed using keys commonly created by formulas
    - Why hashing?:
        - time efficient in case of SEARCH operation O(1) if there are no collisions, but Order(N) if there are many
        collisions
    - Hash function: a function that can be used to map arbitrary size of data to fixed size
    - Key: input data by user
    - Hash value: a value that is returned by hash function
    - Hash table: it is a data structure which implements associative array abstract data type, a structure that can
    map keys to values
    - Collision: a collision occurs when two different keys to a hash function produce the same output

    1.1.Properties of good Hash Function:
        - it distributes hash values uniformly across hash tables
        - it has to use all the input data

2.Collision Resolution Technique
    2.1.Direct Chaining: implements the buckets as Linked List.
        Colliding elements are stored in this list.
        (In this case the hash table can never be full)
    2.2.Open Addressing: colliding elements are stored in other vacant buckets.
        During storage and lookup these are found through so called probing.
        (When table is full - create 2X size of current Hash Table and recal hashing for current keys)
        - Linear Probing: it places new key into the closest following empty cell
        - Quadratic Probing: adding arbitrary quadratic polynomial to the index until
        an empty cell is found
        - Double Hashing: interval between probes is computed by another hash function

3.Hash Tables:
    - If the input size is known, we always use 'open addressing'
    - If we perform deletion operation frequently, we use 'direct chaining'

4.Practical Use of Hashing
'''

#mod function
def mod(number, cell_number):
    return number % cell_number

#ASCII function
def modASCII(string, cell_number):
    total = 0
    for i in string:
        total += ord(i)
    return total % cell_number