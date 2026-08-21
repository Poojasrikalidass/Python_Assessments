""" Question 2: make_introduction """
"""
Inputs: two strings representing a name and a hobby
Output: a string of the form "My name is {name} and I like {hobby}"
"""
def make_introduction(name, hobby):
    return "My name is "+name+" and I like "+hobby

""" Test 2 """
def test_make_introduction():
    print("Testing make_introduction...", end="")
    assert(make_introduction("shriman", "cricket") == "My name is shriman and I like cricket")
    assert(make_introduction("pranav", "cricket") == "My name is pranav and I like cricket")
    assert(make_introduction("Rei", "reading") == "My name is Rei and I like reading")
    assert(make_introduction("Govind", "dancing") == "My name is Govind and I like dancing")
    print("... done!")

if __name__ == '__main__':
    test_make_introduction()