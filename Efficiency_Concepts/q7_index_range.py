  
""" Question 7: index_range """
"""
Inputs: list L and integer target
Output: indexes where target first and last appears in L
"""
def index_range(L, target):
    first=-1
    low,high=0,len(L)-1
    while low<=high:
        mid=(low+high)//2
        if L[mid]==target:
            first=mid
            high=mid-1
        elif L[mid]<target:
            low=mid+1
        else:
            high=mid-1
    
    last=-1
    low,high=0,len(L)-1
    while low<=high:
        mid=(low+high)//2
        if L[mid]==target:
            last=mid
            low=mid+1
        elif L[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return ([first,last])

""" Test 7"""  
def test_index_range():
    print("Testing index_range...", end="")
    assert(index_range([1, 1, 2, 3, 3, 3], 1) == [0, 1])
    assert(index_range([1, 1, 2, 3, 3, 3], 2) == [2, 2])
    assert(index_range([1, 1, 2, 3, 3, 3], 3) == [3, 5])
    assert(index_range([1, 1, 2, 3, 3, 3], 4) == [-1, -1])
    print("Passed!")


if __name__ == '__main__':
    test_index_range()