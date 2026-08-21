""" Question 5: Fix the Runtime Errors """
def compute_total(total, tax):
    final = total + total*tax
    print("Your total is " , final , " dollars.")
    return final

""" Test 5 """
def test_compute_total():
    import math # we use math.isclose to compare floats
    print("Testing compute_total...", end="")
    assert(math.isclose(compute_total(12, 0.05), 12.6))
    assert(math.isclose(compute_total(15, 0.07), 16.05))
    assert(math.isclose(compute_total(5.75, 0), 5.75))
    print("... done!")

if __name__ == '__main__':
    test_compute_total()