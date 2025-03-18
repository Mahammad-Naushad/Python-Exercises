"""
Given a list, count how many unique elements are present
"""


def count_unique_elements(items):
    unique_list = []

    for item in items:
        if item not in unique_list:
            unique_list.append(item)

    return len(unique_list)


my_list = list(map(int, input("Enter numbers followed by space: ").split()))
print(f"Given List is {my_list}")
print(f"Total unique element in list is {count_unique_elements(my_list)}")
