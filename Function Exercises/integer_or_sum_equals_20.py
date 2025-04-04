"""
Given two integers
return True if sum of the integers are 20 or if the integer itself is 20
"""


def check_sum_or_integer(num1, num2):
    return num1 + num2 == 20 or num1 == 20 or num2 == 20


while True:
    input_list = input("Enter two numbers separated by a space: ").split()

    if len(input_list) != 2:
        print("Please enter only 2 integers")
    else:
        number1, number2 = map(int, input_list)
        break

if check_sum_or_integer(number1, number2):
    print("True")
else:
    print("False")