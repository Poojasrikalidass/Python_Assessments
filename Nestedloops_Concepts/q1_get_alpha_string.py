""" Question 1: get_alpha_string """
"""
Input: 2D list
Output: string of all the letters in the list, reading left to right, top to bottom
"""
def is_alpha(s):
    if (s == ""): return False
    for c in s:
        if(("a" <= c <= "z") or ("A" <= c <= "Z")):
             return True
    return False

def get_alpha_string(lst):
    result=""
    for i in lst:
        for j in i:
            if is_alpha(j):
                result+=j
    return result

""" Test 1 """
def test_get_alpha_string():
    print("Testing get_alpha_string...", end="")
    lst1 = [ ['0', '1', 'a'],
             ['2', 'c', 'e'],
             ['3', '4', '5'] ]
    assert(get_alpha_string(lst1) == "ace")
    lst2 = [ [ '0',  '1'],
             ['!?', '45'] ]
    assert(get_alpha_string(lst2) == "")
    lst3 = [ [ 'a', 'l', 'p', 'h' ],
             [ 'a', 'b', 'e', 't' ] ]
    assert(get_alpha_string(lst3) == "alphabet")
    print("... done!")

if __name__ == '__main__':
    test_get_alpha_string()