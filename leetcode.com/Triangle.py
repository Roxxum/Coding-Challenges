"""
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 
Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:
Input: triangle = [[-10]]
Output: -10

 
Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4
"""

# define an input for testing purposes
triangle = [[-1],[2,3],[1,-1,-3]]

# actual code to submit
def solution(triangle):
    answer = triangle[0][0]
    pos = 1

    for i in range(1, len(triangle)):
        pos = triangle[i].index(sorted(triangle[i][pos-1:pos+2])[0])
        answer += triangle[i][pos]
        # TODO: this could cause a wrong index if you were suppose to stop at index 1 in the next list
        if pos < 1:
            pos = 1

    return answer

# use print statement to check if it works
print(solution(triangle))