#1.
def sum_product(t):
    sum_result = 0
    product_result = 1

    for num in t:
        sum_result += num
        product_result *= num

    return sum_result, product_result

#2.
def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError('Input tuples must be of the same length.')

    result = tuple(a+b for a, b in zip(t1, t2))
    #use the 'zip' function to pair the corresponding elements of the input tuples
    print(result)

tuple_elementwise_sum((1,2,3), (1,1,1))

#3.
def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

#4.
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

#5.
def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

#6.
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))
