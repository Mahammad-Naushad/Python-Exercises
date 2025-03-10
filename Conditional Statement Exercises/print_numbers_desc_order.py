"""
Given a number x, the task is to print the numbers from x to 0 in decreasing order in a single line
"""


def print_desc_order(num):
    string = ""
    while num >= 0:
        string += str(num) + " "
        num -= 1

    return string.strip()


number = int(input("Enter a number: "))
print(print_desc_order(number))
