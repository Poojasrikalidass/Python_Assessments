""" Question 7: nth_fibonacci_number """
"""
Input: integer n
Output: nth fibonacci number
"""
def nth_fibonacci_number(n):
    Phi=(1+(5)**0.5)/2
    phi=(1-(5)**0.5)/2
    a=(Phi**n-phi**n)/5**0.5
    result=round(a)
    return result

""" Test 7 """
def test_nth_fibonacci_number():
    print("Testing nth_fibonacci_number...", end="")
    assert(nth_fibonacci_number(1) == 1)
    assert(nth_fibonacci_number(3) == 2)
    assert(nth_fibonacci_number(7) == 13)
    assert(nth_fibonacci_number(10) == 55)
    print("... done!")

if __name__ == '__main__':
    test_nth_fibonacci_number()