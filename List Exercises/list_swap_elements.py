"""
Given a list, swap any two elements by their indexes
"""


def get_input():
    items = list(map(int, input("Enter numbers each separated by a space: ").split()))
    while True:
        swap_choice = input("Enter your choice of swapping? index/value: ").lower()
        is_index_or_value(swap_choice, items)


def is_index_or_value(value, items):
    if value == "index":
        swap_index(items)
        exit(0)
    elif value == "value":
        swap_values(items)
        exit(0)
    else:
        print("Invalid input")


def swap_index(items):
    first_index, second_index = map(int, input("Enter the index of both elements(separated by a space): ").split())
    items[first_index], items[second_index] = items[second_index], items[first_index]
    print(items)


def swap_values(items):
    first_value, second_value = map(int, input("Enter the values of both elements(separated by a space): ").split())
    first_index = items.index(first_value)
    second_index = items.index(second_value)
    items[first_index], items[second_index] = items[second_index], items[first_index]
    print(items)


get_input()
