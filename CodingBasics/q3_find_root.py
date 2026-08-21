""" Question 3: find_root """
"""
Inputs: three integers a, b, c
Output: the positive quadratic root of the equation ax^2 + bx + c = 0
        (using the quadratic formula)
"""
def find_root(a, b, c):
    formula=(-b+(b**2-4*a*c)**0.5)/(2*a)
    return formula

""" Test 3 """
def test_find_root():
    import math # we use math.isclose to compare floats
    print("Testing find_root...", end="")
    assert(math.isclose(find_root(1, -7, 10), 5))
    assert(math.isclose(find_root(1, 0, -9), 3))
    assert(math.isclose(find_root(10, -29, -21), 3.5))
    assert(math.isclose(find_root(1, -2, 1), 1))
    print("... done!")


if __name__ == '__main__':
    test_find_root()