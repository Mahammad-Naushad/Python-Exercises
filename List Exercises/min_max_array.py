"""
Given an array, find the minimum and maximum elements in the array
"""

# Function to find out minimum and maximum in a list
def find_min_max(array):
    minimum = maximum = array[0]

    for i in range(1, len(array)):
        if array[i] > maximum:
            maximum = array[i]
        if array[i] < minimum:
            minimum = array[i]
    return maximum, minimum


# Read list and call function
my_list = list([1, 5, 26, 18, 10])
maximum, minimum = find_min_max(my_list)
print(my_list)
print(f"Maximum of the give list is: {maximum} \nMinimum of the given list is: {minimum} ")
