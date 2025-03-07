"""
You are given a string, you need to return True if  the words "cat" and "hat" appear same number of times in string, otherwise return False
"""


def check_for_equal_occurence(string):
    cat_count = 0
    hat_count = 0
    for i in range(len(string)-2):
        if string[i] == "c" and string[i:i + 3] == "cat":
            cat_count += 1
        elif string[i] == "h" and string[i:i + 3] == "hat":
            hat_count += 1

    return cat_count == hat_count


string = input("Enter the string: ").lower()

print(check_for_equal_occurence(string))

