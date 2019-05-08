def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if number == input_list[0]:
        return 0
    elif number < input_list[0]:
        index = len(input_list) - 1
        while number < input_list[index]:
            index -= 1
            if input_list[index] > input_list[index + 1]:
                break
        return index if number == input_list[index] else -1
    else:
        index = 1
        while number > input_list[index]:
            if input_list[index] > input_list[index + 1]:
                break
            index += 1
        return index if number == input_list[index] else -1
    pass

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