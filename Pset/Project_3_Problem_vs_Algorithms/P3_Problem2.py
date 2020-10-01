def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array): Input array to search
       number (int): target to search
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(input_list) - 1
    while left <= right:
        mid = (left+right) // 2
        if number == input_list[mid]:
            return mid
        if input_list[left] <= input_list[mid]:
            if input_list[left] <= number <= input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if input_list[mid] <= number <= input_list[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


#%% Testing - Official
# Normal cases
print('Normal Cases:')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# Pass
print('\n')

# Edge cases
print('Edge Cases:')
test_function([[], 9])
# Pass
test_function([[1], 9])
# Pass