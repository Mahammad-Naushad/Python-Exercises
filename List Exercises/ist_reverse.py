"""
Program to reverse a list
"""


def reverse_list(my_list):
    # Using a built-in function
    my_list.reverse()
    print(f"Using a built in function reverse(): {my_list}")

    reversed_list = []
    # Using a loop
    for i in my_list:
        reversed_list.insert(0, i)

    print(f"Using a loop: {reversed_list}")


items = list(map(int, input("Enter numbers separated by a space: ").split()))
reverse_list(items)