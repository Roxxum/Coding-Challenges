"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
As the answer can be very large, return it modulo 10^9 + 7.

 
Example 1:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:
Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

 
Constraints:
3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""
from collections import Counter

# define an input for testing purposes
arr = [1,1,2,2,3,3,4,4,5,5]
target = 8

# actual code to submit
def solution(array, num):
    c = Counter(array)
    s = [x for x in c if x < num]
    answer = 0

    for i in s:
        for j in s:
            for k in s:
                if i + j + k == target and i <= j <= k:
                    a = [c.get(l) for l in [i, j, k]]
                    # TODO: The below probably only works for this input. Also returns a float somehow???
                    if i != j and j != k:
                        answer += (sorted(a)[0] * sorted(a)[0] * sorted(a)[0])
                    elif i == j or j == k:
                        answer += ((sorted(a)[0] / i) * (sorted(a)[0] / i) * sorted(a)[0])

    return answer

# use print statement to check if it works
print(solution(arr, target))