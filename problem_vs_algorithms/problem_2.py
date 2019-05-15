def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(list): Input array to search
       number(int): The target
    Returns:
       int: Index or -1
    """
    right = len(input_list) - 1
    mid = right // 2
    left = 0
    while number != input_list[mid]:
        tmp = mid
        if number > input_list[left]:
            mid = (mid + left) // 2
            left = tmp
        elif number < input_list[left]:
            mid = (mid + right) // 2
            right = tmp
        else:
            return left
        if mid == tmp:
            return -1
    return mid


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


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 0])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 20])
test_function([[6, 7, 8, 1, 2, 3, 4], -1])
