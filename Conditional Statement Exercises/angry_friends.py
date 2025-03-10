"""
Problem Statement:
There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry.
You are in trouble if both of them are angry or no one of them is angry.
"""


def anger_state(j_angry, s_angry):
    if (j_angry and s_angry) or (not j_angry and not s_angry):
        return True
    else:
        return False


print("Enter either True or False")
john_angry = input("Enter John's anger status: ") == "True"
smith_angry = input("Enter Smith's anger status: ") == "True"

print(anger_state(john_angry, smith_angry))
