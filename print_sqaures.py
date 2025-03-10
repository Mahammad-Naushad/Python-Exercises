"""
Given a positive integer x, the task is to print the numbers from 1 to x in the order as squares
"""


def get_number():
    number = int(input("Enter a number: "))
    if number <= 0:
        print("Enter positive number")
        return get_number()
    else:
        return number


def print_squares(num):
    string = ""
    i = 1
    while True:
        if i * i <= num:
            string += str(i * i) + " "
            i += 1
        else:
            break

    return string


valid_number = get_number()
print(print_squares(valid_number))

