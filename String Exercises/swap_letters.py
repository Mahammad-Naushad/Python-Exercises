"""
Given a list of strings. Swap all the Gs with letter E and swap all the Es with letter G.
"""


def replace_letters(items):
    new_list = [item.replace('g', '-').replace('e', 'g').replace('-', 'e') for item in items]

    # for item in items:
    #     new_list.append(item.replace('g', 'e'))

    return new_list


my_list = input("Enter each string followed by a space: ").lower().split()
print(f"Current list is {list(my_list)}")

print(replace_letters(my_list))
