""" Question 9: is_alpha """
"""
Input: string s
Output: True if s contains at least one character and every char is a letter
        False otherwise
"""
def is_alpha(s):
    if s=="":
        return False
    for c in s:
        if not (("A"<=c<="Z")or("a"<=c<="z")):
            return False
    return True

""" Test 9 """
def test_is_alpha():
    print("Testing is_alpha...", end='')
    assert(is_alpha("") == False)
    assert(is_alpha("a") == True)
    assert(is_alpha("123a") == False)
    assert(is_alpha("Hello") == True)
    assert(is_alpha("hello!") == False)
    print("... done!")

if __name__ == '__main__':
    test_is_alpha()