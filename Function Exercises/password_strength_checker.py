"""
Given a password, check its strength based on the given parameters:

1. At least 8 characters long.
2. Contains at least one uppercase letter.
3. Contains at least one lowercase letter.
4. Contains at least one digit.
5. Contains at least one special character (!@#$%^&*()).
"""


def length_check(my_password):
    return len(my_password) >= 8


def uppercase_check(my_password):
    return any(word.isupper() for word in my_password)


def lowercase_check(my_password):
    return any(word.islower() for word in my_password)


def number_check(my_password):
    return any(word.isdigit() for word in my_password)


def special_character_check(my_password):
    return not my_password.isalnum()


def check_strength(my_result):
    if sum(my_result) == 5:
        print("Your password is strong")
    elif sum(my_result) >= 3:
        print("Your password is medium")
    else:
        print("Your password is weak")


print("This program is created to check the strength of your password")
password = input("Enter your password: ")

results = [length_check(password), uppercase_check(password), lowercase_check(password), number_check(password),
           special_character_check(password)]

check_strength(results)

