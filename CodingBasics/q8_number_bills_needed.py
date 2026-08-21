""" Question 8: Fix the Errors """
"""
Input: cost
Output: least number of $20, $5, and $1 bills needed to cover cost
"""
def number_bills_needed(cost):
    num_twenty = cost // 20
    cost = cost - num_twenty * 20
    num_five = cost // 5
    cost = cost - num_five * 5
    num_one = cost
    return num_twenty + num_five + num_one

""" Test 8 """
def test_number_bills_needed():
    print("Testing number_bills_needed...", end="")
    assert(number_bills_needed(42) == 2 + 0 + 2)
    assert(number_bills_needed(17) == 0 + 3 + 2)
    assert(number_bills_needed(79) == 3 + 3 + 4)
    assert(number_bills_needed(4) == 0 + 0 + 4)
    assert(number_bills_needed(5) == 0 + 1 + 0)
    print("... done!")

if __name__ == '__main__':
    test_number_bills_needed()