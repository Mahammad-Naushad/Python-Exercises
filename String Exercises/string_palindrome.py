"""
Given a string, check whether it's a palindrome or not
"""


def palindrome_check(my_string):
    for index in range(len(my_string) // 2):
        if my_string[index] != my_string[-1 - index]:
            return False

    return True


word = input("Enter a string: ").lower()

if palindrome_check(word):
    print(f"Yes, {word} is a palindrome")
else:
    print(f"No, {word} is not a palindrome")
