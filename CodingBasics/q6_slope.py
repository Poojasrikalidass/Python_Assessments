""" Question 6: Fix the Logical Errors """
def slope(x1, y1, x2, y2):
    result =( y2 - y1) / (x2 - x1)
    return result

""" Test 6 """
def test_slope():
    import math # we use math.isclose to compare floats
    print("Testing slope...", end="")
    assert(math.isclose(slope(1, 3, 6, 5), 0.4))
    assert(math.isclose(slope(2, 4, 6, 8), 1))
    assert(math.isclose(slope(0, 2, 5, -2), -0.8))
    print("... done!")

if __name__ == '__main__':
    test_slope()