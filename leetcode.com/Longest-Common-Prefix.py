"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

 
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

# define an input for testing purposes
strs = ["dog","racecar","car"]
# this should return 'car'

# actual code to submit
prefix = ''

# TODO: this is actually so bad and literally only works for one type of prefix
def checking(index):
    global prefix
    check = strs[0][index]
    for i in range(len(strs)):
        if strs[i][index] == check:
            if i >= len(strs)-1:
                prefix += strs[i][index]
            else:
                pass
        else:
            break

for i in range(len(strs)):
    checking(i)

# use print statement to check if it works
print(prefix)