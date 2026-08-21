""" Question 10: is_alpha_num """
"""
Input: string s
Output: True if s contains at least one character and each char is a letter or digit
        False otherwise
"""

def is_alpha(s):
    if s == 0:
        return False
    
    for c in s:
        if not (('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            return False
    
    return True


def is_digit(s):
    if s == 0:
        return False
    
    for c in s:
        if not ('0' <= c <= '9'):
            return False
    
    return True

def is_alpha_num(s):
    if s=="":
        return False
    for c in s:
        if not((is_alpha(c))or(is_digit(c))):
            return False
    return True

""" Test 10 """
def test_is_alpha_num():
    print("Testing is_alpha_num...", end='')
    assert(is_alpha_num("") == False)
    assert(is_alpha_num("a") == True)
    assert(is_alpha_num("123a") == True)
    assert(is_alpha_num("Hello") == True)
    assert(is_alpha_num("hello!") == False)
    print("... done!")


if __name__ == '__main__':
    test_is_alpha_num()