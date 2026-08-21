""" Question 1: n_ones """
"""
Input: integer n
Output: integer with n 1s
"""
def n_ones(n):
    num=0
    for i in range(n):
        num+=10**i
    return num

  

""" Test 1 """
def test_n_ones():
    print("Testing n_ones...", end='')
    assert(n_ones(0) == 0)
    assert(n_ones(1) == 1)
    assert(n_ones(4) == 1111)
    assert(n_ones(7) == 1111111)
    print("... done!")


if __name__ == '__main__':
    test_n_ones()
