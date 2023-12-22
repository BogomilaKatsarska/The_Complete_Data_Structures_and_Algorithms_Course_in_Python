words_example = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']


def count_word_frequency(words):
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(count_word_frequency(words_example))


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


def max_value_key(dict1):
    return max(dict1, key=dict1.get)


def reverse_dict(dict1):
    return {v: k for k, v in dict1.items()}


def filter_dict(dict, condition):
    return {k: v for k,v in dict.items() if condition(k, v)}


def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
    return count_elements(list1) == count_elements(list2)
