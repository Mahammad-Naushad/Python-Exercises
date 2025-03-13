"""
Given a list, find the second smallest and second largest element
"""


def get_second_smallest_largest(item):
    # Method 1
    item.sort()
    print(f"Second smallest is {item[1]} and second largest is {item[-2]}")

    # Method 2
    item.remove(min(item))
    item.remove(max(item))
    print(f"second smallest is {min(item)} and second largest is {max(item)}")

    # Method 3
    smallest, second_smallest = item[0], item[1]
    largest, second_largest = item[0], item[1]

    print(item)
    for index in range(2, len(item)):
        if item[index] < smallest:
            second_smallest = smallest
            smallest = item[index]
        elif item[index] < second_smallest:
            second_smallest = item[index]

        if item[index] > largest:
            second_largest = largest
            largest = item[index]
        elif item[index] > second_largest:
            second_largest = item[index]

    print(f"second smallest is {second_smallest} and second largest is {second_largest}")


my_list = list(map(int, input("Enter a number separated by a space: ").split()))
get_second_smallest_largest(my_list)