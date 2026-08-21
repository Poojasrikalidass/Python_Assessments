""" Question 6: average_of_primes """
"""
Input: list of integers
Output: average of prime numbers in list
"""
def is_prime(num):
    if (num <= 1):
        return False
    for possible_factor in range(2, num):
        if (num % possible_factor == 0):
            return False
    return True

def average_of_primes(L):
    sum = 0
    count = 0
    

    for i in L:
        if is_prime(i):
            sum += i
            count += 1
    if count == 0:
        return 0

        

    average = sum / count
    return average

""" Test 6 """
import math
def test_average_of_primes():
    print("Testing average_of_primes...", end='')
    assert(average_of_primes([]) == 0)
    assert(average_of_primes([2]) == 2)
    assert(average_of_primes([1, 2, 3]) == 2.5)
    assert(average_of_primes([4, 6, 8]) == 0)
    assert(average_of_primes([2, 3, 5, 7, 11]) == 5.6)
    print("... done!")


if __name__ == '__main__':
    test_average_of_primes()