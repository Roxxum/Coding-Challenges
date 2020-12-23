"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false.
 

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:
1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
"""

# define an input for testing purposes
nums = [20,100,10,12,5,13]
# this should return true because 10 > 12 > 13

# actual code to submit
# TODO: this solution does not work for nonconsecutive index positions 
solution = False
length = len(nums)

for i in range(len(nums)-2):
    if nums[i] < nums[i+1] < nums[i+2]:
        solution = True

# use print statement to check if it works
print(solution)