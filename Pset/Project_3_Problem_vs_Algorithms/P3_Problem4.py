def sort_012(input_list):
    """
    The idea is to put 0 and 2 in their correct positions, which will make sure
    all the 1s are automatically placed in their right positions
    """
    # initialize pointers for next positions of 0 and 2
    next_pos_0 = 0
    next_pos_2 = len(input_list) - 1

    front = 0

    while front <= next_pos_2:
        if input_list[front] == 0:
            input_list[front] = input_list[next_pos_0]
            input_list[next_pos_0] = 0
            next_pos_0 += 1
            front += 1
        elif input_list[front] == 2:           
            input_list[front] = input_list[next_pos_2] 
            input_list[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front += 1
    
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Testing
test1 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test1)
# sorted: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

test2 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test2)
# sorted: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]

test3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_function(test3)
# sorted: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]