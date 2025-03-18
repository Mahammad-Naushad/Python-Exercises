"""
Given a list of strings. reverse the string for each element in a list
"""


def reverse_string(items):
    new_list = [item[::-1] for item in items]

    return new_list


my_list = input("Enter strings followed by a space: ").split()

print(reverse_string(my_list))
