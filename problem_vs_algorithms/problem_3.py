def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    input_list = sorted(input_list, reverse=True)
    number1 = ''
    number2 = ''
    flag = True
    for number in input_list:
        if flag:
            number1 += str(number)
            flag = False
        else:
            number2 += str(number)
            flag = True
    return [int(number1), int(number2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print(output)
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
