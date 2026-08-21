""" Question 7: is_digit """
"""
Input: string s
Output: True if s contains at least one character and every char is a digit
        False otherwise
"""
def is_digit(s):
    if s=="":
        return False
    for i in s:
        if not ("0" <= i <= "9"):
            return False
    return True
    

""" Test 7 """
def test_is_digit():
    print("Testing is_digit...", end='')
    assert(is_digit("") == False)
    assert(is_digit("1") == True)
    assert(is_digit("123a") == False)
    assert(is_digit("99923") == True)
    assert(is_digit("abcd") == False)
    print("... done!")

if __name__ == '__main__':
    test_is_digit()