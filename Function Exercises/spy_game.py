"""
Given a list, check if it contains 0 0 7 in order
If Yes, return True else False
"""


def check_spy_numbers(numbers):
    for index in range(0, len(numbers) - 2):
        if numbers[index: index + 3] == [0, 0, 7]:
            return True

    return False


while True:
    try:
        my_list = list(map(int, input("Enter numbers separated by a space: ").split()))
        break
    except ValueError:
        print("Enter integers only!!")

if check_spy_numbers(my_list):
    print(f"True, [0, 0, 7] is present in {my_list}")
else:
    print(f"False, [0, 0, 7] is not present in {my_list}")
