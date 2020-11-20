"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 
Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

# define an input for testing purposes
intervals = [[1,3],[2,6],[8,10],[15,18]]

#actual code to submit
sort = sorted(intervals)
count = 0
for i in sort:
    length = len(sort)
    if count < length-1:
        if sort[count][1] >= sort[count+1][0]:
            sort[count][1] = sort[count+1][1]
            sort.remove(sort[count+1])
        if length > count-1:
            count += 1

#use print statement to check if it works
print(sort)