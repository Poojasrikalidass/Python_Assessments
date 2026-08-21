""" Question 11: collatz """
"""
Input: integer n
Output: number of steps it takes to reach 1 from n following the Collatz Conjecture
"""
def collatz(n):
    step=0
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        step+=1
    return step

""" Test 11 """
def test_collatz():
    print("Testing collatz...", end='')
    assert(collatz(1) == 0)
    assert(collatz(2) == 1)
    assert(collatz(5) == 5)
    assert(collatz(11) == 14)
    assert(collatz(50) == 24)
    print("... done!")


if __name__ == '__main__':
    test_collatz()