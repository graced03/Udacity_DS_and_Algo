#%% Imports and functions declarations
import random
import math

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return None

    max_value = - float("inf")
    min_value = float("inf")

    for num in ints:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return (min_value, max_value)

#%% Testing - Official
# Normal cases
print('Normal Cases:')
# Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Case 2
l = [i for i in range(-4, 4)]  # a list containing -12 - 24
random.shuffle(l)
print("Pass" if ((-4, 3) == get_min_max(l)) else "Fail")
print('\n')

# Edge cases
print('Edge Cases:')
# Case 3
l = [i for i in range(1, 2)]  # a list containing 300
random.shuffle(l)
print("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

# Case 4
l = []  # an empty list
print("Pass" if (None == get_min_max(l)) else "Fail")

# Case 5
l = [i for i in range(-10, -1)]  # a list containing -24 - -2
random.shuffle(l)
print("Pass" if ((-10, -2) == get_min_max(l)) else "Fail")