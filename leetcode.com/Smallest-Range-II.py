"""
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).
After this process, we have some array B.
Return the smallest possible difference between the maximum value of B and the minimum value of B.

 
Example 1:
Input: A = [1], K = 0
Output: 0
Explanation: B = [1]

Example 2:
Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]

Example 3:
Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]
 

Constraints:
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""

# define an input for testing purposes
A = [2,7,2]
K = 1

# actual code to submit
B = []

for i in range(len(A)):
    if A[i] > K:
        B.append(A[i] - K)
    else:
        B.append(A[i] + K)

B = sorted(B)

# use print statement to check if it works
print(B[-1] - B[0])