import sys


def get_min_max_by_sorting(input_list):
    """
    Return a tuple(min_val, max_val) out of list of unsorted integers.

    Args:
        input_list(list): List of integers containing one or more integers
    Returns:
        (int),(int): Minimum and maximum value
    """
    min_val = sys.maxsize
    max_val = -sys.maxsize - 1
    for num in input_list:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    return min_val, max_val


# Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")
