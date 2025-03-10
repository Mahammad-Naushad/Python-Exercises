"""
You are given a number N, you need to print its multiplication table(till 10)
"""


def generate_multiplication_table(number):
    for i in range(1,11):
        print(f"{number} * {i} = {number*i}")


num = int(input("Enter a number: "))

generate_multiplication_table(num)
