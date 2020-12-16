"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.


Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2 <= n <= 10
100 <= A[] <= 100

Sample Input:
5
2 3 6 6 5

Sample Output:
5

Explanation:
Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
"""

# define an input for testing purposes
n = 5
A = [2,3,6,6,5]
second = []

# actual code to submit
A.sort(reverse=True)

for i in range(1, n-1):
    if A[0] > A[i]:
        if A[i] > A[i+1]:
            second.append(A[i])
            break

# use print statement to check if it works
print(second)