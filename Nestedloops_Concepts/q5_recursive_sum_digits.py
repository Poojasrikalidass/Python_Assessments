
""" Question 5: recursive_sum_digits """
"""
Input: integer n
Output: sum of digits in n
        must be solved recursively
"""
def recursive_sum_digits(n):
    n=abs(n)
    if n==0:
        return 0
    else:
       partial=recursive_sum_digits(n//10)
       return n%10 + partial

""" Test 5 """
def test_recursive_sum_digits():
    print("Testing recursive_sum_digits...", end="")
    assert(recursive_sum_digits(5) == 5)
    assert(recursive_sum_digits(31) == 4)
    assert(recursive_sum_digits(123) == 6)
    assert(recursive_sum_digits(0) == 0)
    assert(recursive_sum_digits(-524) == 11)
    assert(recursive_sum_digits(719340) == 24)
    print("... done!")

if __name__ == '__main__':
    test_recursive_sum_digits()