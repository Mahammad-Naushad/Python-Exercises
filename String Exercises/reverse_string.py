"""
Given a string, reverse the order of words
"""


def reverse_string(words):
    words = words.split(' ')

    return " ".join(words[::-1])


my_string = input("Enter a string: ")
print(reverse_string(my_string))
