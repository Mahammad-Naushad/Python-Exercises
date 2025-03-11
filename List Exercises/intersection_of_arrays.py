"""
Given two sorted arrays arr1[] and arr2[]. Your task is to return the intersection of both arrays.
"""


def array_intersection(a, b):
    print(list(set(a).intersection(set(b))))


a = [1, 2, 3, 4, 5]
b = [2, 4, 5]
array_intersection(a, b)
