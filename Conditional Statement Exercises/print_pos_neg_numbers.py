"""
You are given a number n.The number n can be negative or positive.
If n is negative, print numbers from n to 0.
If positive, print numbers from n to 0.
"""


def get_number():
    while True:
        number = int(input("Enter a number: "))

        if number == 0:
            print(number)
            exit(0)
        elif number < 0:
            print(print_negative_numbers(number))
            break
        else:
            print(print_positive_numbers(number))
            break


def print_negative_numbers(num):
    string = ""
    while num <= 0:
        string += str(num) + " "
        num += 1

    return string.rstrip()


def print_positive_numbers(num):
    string = ""
    while num >= 0:
        string += str(num) + " "
        num -= 1

    return string.rstrip()


get_number()