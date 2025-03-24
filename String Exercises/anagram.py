"""
Given 2 lower case strings, check whether they're anagrams or not
"""


def check_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    else:
        dict1 = count_letters(string1)
        dict2 = count_letters(string2)

    return dict1 == dict2


def count_letters(string1):
    dict1 = {}

    for letter in string1:
        if letter in dict1:
            dict1[letter] += 1
        else:
            dict1[letter] = 1

    return dict1


first_string, second_string = input("Enter two strings separated by a space: ").lower().split()

if check_anagram(first_string, second_string):
    print(f"Yes, {first_string} and {second_string} are anagram of each other")
else:
    print(f"No, {first_string} and {second_string} are not anagram of each other")


