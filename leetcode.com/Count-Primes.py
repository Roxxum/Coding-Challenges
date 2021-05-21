"""
Count the number of prime numbers less than a non-negative number, n.
 

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

 
Constraints:
0 <= n <= 5 * 10^6
"""

# define an input for testing purposes
n = 99999

# actual code to submit
def solution(input):
    primes = [2, 3]
    #TODO: this is by far the slowest way i could have possibly coded this. just wow
    if n < 3:
        return 0
    elif n == 3:
        return 1
    else:
        for i in range(4, n):
            for j in primes:
                if i % j == 0:
                    break
                else:
                    if primes.index(j) == len(primes)-1: 
                        primes.append(i)

        return len(primes)

# use print statement to check if it works
print(solution(n))