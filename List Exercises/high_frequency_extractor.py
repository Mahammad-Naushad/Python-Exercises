"""
Given a list and a frequency of occurence of an element, print only those elements whose frequency is higher
"""


def high_frequency_list(items, counter):
    new_list = [item for item in items if items.count(item) > counter]

    return list(set(new_list))


my_list = list(map(int, input("Enter numbers followed by a space: ").split()))
frequency = int(input("Enter the frequency: "))

print(f"Given list is {my_list}")
print(f"Frequency given is {frequency}")
print(f"Elements which occurs more than {frequency} times are {high_frequency_list(my_list, frequency)}")


