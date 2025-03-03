'''Given two integer variables a and b, and a boolean variable flag.

The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.

Otherwise, return False.
'''

num1, num2 = map(int, input("Enter two integers: ").split())
flag = bool(input("Enter a value for flag: ")) == "True"

if ((num1 >= 0 or num2 >= 0) and flag is False) or ((num1 < 0 and num2 < 0) and flag is True):
    print("True")
else:
    print("False")
