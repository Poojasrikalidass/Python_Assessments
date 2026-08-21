""" Question 4: recursive_match """
"""
Input: two lists
Output: number of indexes in the two lists where the values match
        must be solved recursively
"""
def recursive_match(lst1, lst2):
    if lst1==[] or lst2==[]:
        return 0
    else:
        partial=recursive_match(lst1[1:],lst2[1:])
        if lst1[0]==lst2[0]:
            return partial+1
        else:
            return partial
 

""" Test 4 """
def test_recursive_match():
    print("Testing recursive_match...", end="")
    assert(recursive_match([4, 2, 1, 6], [4, 3, 7, 6]) == 2)
    assert(recursive_match([1, 2, 3, 4], [4, 3, 2, 1]) == 0)
    assert(recursive_match([5, 6, 7, 8, 9, 10], [0, 6, 7, 8]) == 3)
    assert(recursive_match([], [100, 200]) == 0)
    print("... done!")


if __name__ == '__main__':
    test_recursive_match()