"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists
"""

# define an input for testing purposes
nums = [-5,2,5,9,11,15]
target = 16

# actual code to submit
length = len(nums)
solved = []

for i in range(length):
    for z in range(i + 1, length):
        if nums[i] + nums[z] == target:
            solved.extend((i, z))

# use print statement to check if it works
print(solved)