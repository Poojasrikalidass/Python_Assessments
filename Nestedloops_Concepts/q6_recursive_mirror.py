""" Question 6: recursive_mirror """
"""
Input: string s
Output: string containing s and mirror of s
        must be solved recursively
"""
def recursive_mirror(s):
    if s=="":
        return ""
    else:
        smaller=s[1:]
        partial=recursive_mirror(smaller)
        return s[0]+partial+s[0]
    
    

""" Test 6 """
def test_recursive_mirror():
    print("Testing recursive_mirror...", end="")
    assert(recursive_mirror("hello") == "helloolleh")
    assert(recursive_mirror("wow") == "wowwow")
    assert(recursive_mirror("code") == "codeedoc")
    assert(recursive_mirror("recursion") == "recursionnoisrucer")
    assert(recursive_mirror("") == "")
    print("... done!")

if __name__ == '__main__':
    test_recursive_mirror()
