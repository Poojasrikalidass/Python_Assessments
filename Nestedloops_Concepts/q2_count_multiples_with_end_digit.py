""" Question 2: count_multiples_with_end_digit """
"""
Input: two integers
Output: all multiples of n between 1xn and nxn that end in specified digit
"""
def count_multiples_with_end_digit(n, digit):
    count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            product=i*j
            if product%10==digit:
                count+=1
    return count

""" Test 2 """
def test_count_multiples_with_end_digit():
    print("Testing count_multiples_with_end_digit...", end="")
    assert(count_multiples_with_end_digit(6, 2) == 6)
    assert(count_multiples_with_end_digit(5, 0) == 4)
    assert(count_multiples_with_end_digit(7, 7) == 2)
    print("... done!")


if __name__ == '__main__':
    test_count_multiples_with_end_digit()