"""
Given a list, return sum of digits of each element
"""


def get_sum(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number = number // 10

    return summ


def sum_digits(my_list):
    list_sum = []
    for item in my_list:
        value = get_sum(item)
        list_sum.append(value)

    return list_sum


items = list(map(int, input("Enter a number separated by space: ").split()))
print(f"New list with sum of each element is : {sum_digits(items)}")

