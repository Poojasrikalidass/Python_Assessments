""" Question 4: Fix the Syntax Errors """
"""
Uncomment the following function and fix the syntax errors so it passes
"""
def tens_digit(n):
     n = n // 10 
     return n % 10

""" Test 4 """
def test_tens_digit():
    print("Testing tens_digit...", end="")
    assert(tens_digit(1234) == 3)
    assert(tens_digit(42) == 4)
    assert(tens_digit(9) == 0)
    print("... done!")

if __name__ == '__main__':
    test_tens_digit()