""" Question 5: longest_string_length """
"""
Input: list of strings
Output: length of longest string in list
"""
def longest_string_length(L):
    longest = 0
    
    for i in L:
        if len(i) > longest:
            longest = len(i)
    
    return longest

   

""" Test 5 """
def test_longest_string_length():
    print("Testing longest_string_length...", end='')
    L0 = ["hi", "hello", "howdy"]
    assert(longest_string_length(L0) == 5)
    L1 = ["hello", "goodbye", "pineapple"]
    assert(longest_string_length(L1) == 9)
    L2 = ["a", "b", "c"]
    assert(longest_string_length(L2) == 1)
    print("... done!")


if __name__ == '__main__':
    test_longest_string_length()