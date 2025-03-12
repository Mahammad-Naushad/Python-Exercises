"""
Simple python program to showcase list operations
"""


def list_operations(my_list):
    # Accessing a list
    print(my_list[0])

    # Changing an item in the list
    my_list[0] = "Hello"
    print(my_list)

    # Add an item to a list insert(), extend(), append()
    my_list.insert(0, "Naushad")
    my_list.extend([6, 7, 8])
    my_list.append([9, 10])

    print(my_list)

    # Removing an item remove(), pop(), del, clear()
    my_list.remove("Hello")
    print(my_list)
    my_list.pop(0)
    print(my_list)
    del my_list[1:4]
    print(my_list)
    my_list.clear()
    print(my_list)


my_list = [1, 2, 3, 4, 5]
list_operations(my_list)

