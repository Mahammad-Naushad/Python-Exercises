"""
Given a list, find if the list contains three consecutive numbers in it
"""


def consecutive_numbers(items):
    length = len(items)
    items.sort()

    for index in range(0, length - 2):
        if items[index + 1] == items[index] + 1 and items[index + 2] == items[index] + 2:
            return True

    return False


my_list = list(map(int, input("Enter numbers followed by a space: ").split()))

print(f"Given list is {my_list}")
print(f"{consecutive_numbers(my_list)}, {my_list} has 3 consecutive numbers")
