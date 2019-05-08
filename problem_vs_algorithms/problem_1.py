def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if (number == 0) or (number == 1):
        return number
    root = number // 2
    prev_big_root = number
    prev_small_root = 1
    while (root > 1):
        square = root**2
        if square == number or root == prev_small_root or root == prev_big_root:
            break
        elif square > number:
            prev_big_root = root
            root = (root + prev_small_root) // 2
        else:
            prev_small_root = root
            root = (root + prev_big_root) // 2
    return root
        

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (5 == sqrt(37)) else "Fail")