def sqrt(number) : 
    if number < 0:
        return None

    # Base cases 
    if (number == 0 or number == 1) : 
        return number
   
    # Do Binary Search for floor(sqrt(x)) 
    start = 1
    end = number // 2
    while (start <= end) : 
        mid = (start + end) // 2

        if mid ** 2 == number: 
            return mid 
        # Since we need floor, we update  
        # answer when mid square is smaller 
        # than the number, and move closer to sqrt(x) 
        elif mid ** 2 < number: 
            start = mid + 1
            root = mid 
        else: 
            # If mid square is greater than our number
            end = mid - 1
              
    return root


# Testing
print ("Pass" if  (3 == sqrt(9)) else "Fail")
# Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")
# Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")
# Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")
# Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Pass

# Edge cases
print(sqrt(-9))
# Results: None
print(sqrt(123456789))
# Results: 11111
