"""
Given an array, interchange first and last elements
"""


def interchange_indexes(items):
    items[0], items[-1] = items[-1], items[0]

    return items


my_list = input("Enter numbers separated by space: ").split()
print(interchange_indexes(my_list))