""" Question 12: longest_bit_run """
"""
Input: string s of 0s and 1s
Output: the length of the longest run of 0s or 1s
"""


def longest_bit_run(s):
    longest=1
    current=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            current+=1
        else:
            current=1
        if current>longest:
            longest=current
    return longest
print(longest_bit_run('001010'))

""" Test 12 """
def test_longest_bit_run():
    print("Testing longest_bit_run...", end='')
    assert(longest_bit_run('0') == 1)
    assert(longest_bit_run('011') == 2)
    assert(longest_bit_run('0000') == 4)
    assert(longest_bit_run('01') == 1)
    assert(longest_bit_run('00111100') == 4)
    print("... done!")


if __name__ == '__main__':
    test_longest_bit_run()