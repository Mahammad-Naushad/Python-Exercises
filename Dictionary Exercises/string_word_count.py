"""
Given a string, find the count of occurrence of each word
"""


def check_word_count(my_word):
    word_dict = dict()

    my_list = my_word.split()
    for word in my_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict


my_string = input("Enter a string: ")
print(f"Word count for {my_string} is as follows: \n{check_word_count(my_string)}")
