"""
You are given a string str, you need to print its characters at even indices
"""


def print_even_indices(string):
    new_string = ""
    for i in range(0, len(string), 2):
        new_string = new_string + string[i]

    return new_string


my_string = input("Enter a string: ")

print(print_even_indices(my_string))
