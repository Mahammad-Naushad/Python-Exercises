"""
Given two arrays, the task is to find the number of elements in the union between these two arrays
"""


# Function to count the items after union
def get_union_count(a, b):
    union_set = set(a).union(set(b))

    print(f"After making a union, count is {len(union_set)}")


# Hardcoded a and b values for simplicity
a = [1, 2, 3, 4, 5]
b = [1, 2, 6]
get_union_count(a, b)
