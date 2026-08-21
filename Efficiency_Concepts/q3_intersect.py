""" Question 3: intersect """
"""
Inputs: two lists, L and K
Output: all elements in K that appear in L, order and duplicates preserved
        must run in linear time
"""
def intersect(L, K):
    S=set(L)
    result=[]
    for x in K:
        if x in S:
            result.append(x)
    return result

""" Test 3 """
def test_intersect():
    print("Testing intersect...", end='')
    L = [1, 2, 2, 3, 0]
    K = [1, 1, 2, 5, 0]
    assert(intersect(L, K) == [1, 1, 2, 0])
    L1 = [6, 7, 8, 9]
    K1 = [2, 7, 7, 7, 5]
    assert(intersect(L1, K1) == [7, 7, 7])
    
    # if your code is failing this test, check the efficiency!
    L2 = [0]*30000
    K2 = [0]*30000
    assert(intersect(L2, K2) == [0]*30000)
    print("... done!")


if __name__ == '__main__':
    test_intersect()