"""
Given two numbers
if two numbers are even, return the lesser of the two
if two of them are odd, return the greater of the two
"""


def check_even_odd(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    elif a % 2 != 0 and b % 2 != 0:
        return max(a, b)
    else:
        return None


number1, number2 = map(int, input("Enter two numbers separated by a space: ").split())
result = check_even_odd(number1, number2)

if check_even_odd(number1, number2) is not None:
    print(result)
else:
    print("one of the number is odd while the other one is even")
