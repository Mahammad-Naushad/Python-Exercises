"""
Given a string, remove duplicate letters
"""


def remove_duplicate_letters(my_string):
    duplicate_string = ""
    new_string = ""

    for letter in my_string:
        if letter not in duplicate_string:
            duplicate_string += letter
            new_string += letter

    return new_string


word = input("Enter a string: ")
print(f"After removing duplicate elements {word} becomes {remove_duplicate_letters(word)}")
