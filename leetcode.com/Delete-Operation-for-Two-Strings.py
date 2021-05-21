"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character in either string.

 
Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4


Constraints:
    1 <= word1.length, word2.length <= 500
    word1 and word2 consist of only lowercase English letters.
"""

from collections import Counter

# define an input for testing purposes
word1 = "sea"
word2 = "ate"
# expected output: 4

# actual code to submit
def solution(word1, word2):
    c = Counter(word1)

    for i in word2:
        if c[i] > 0:
            c[i] -= 1
        else:
            c.update(i)
    # TODO: this does not include checks for swapping character positions     
    return sum(c.values())

# use print statement to check if it works
print(solution(word1, word2))