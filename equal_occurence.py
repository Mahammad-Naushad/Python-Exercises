"""
You are given a string, you need to return True if  the words "cat" and "hat" appear same number of times in string, otherwise return False
"""


def check_for_equal_occurence(string):
    cat_count = 0
    hat_count = 0

    cat_count = string.count("cat")
    hat_count = string.count("hat")

    return cat_count == hat_count


string = input("Enter the string: ").lower()

print(check_for_equal_occurence(string))

