def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = mergesort(input_list)

    num_1 = 0
    num_2 = 0
    for i in range(len(input_list) // 2):
        num_1 += sorted_list[(2*i+1)] * (10**i)
    for i in range(len(input_list) - len(input_list) // 2):
        num_2 += sorted_list[(2*i)] * (10**i)
    return num_1, num_2

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Testing
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

# Edge cases
test_case = [[1,2,2,2,2], [221, 22]]
test_function(test_case)

test_case = [[1, 2], [1, 2]]
test_function(test_case)

test_case = [[], []]
test_function(test_case)