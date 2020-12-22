"""
Given a 32-bit signed integer, reverse digits of an integer.
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

 
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
 

Constraints:
-2^31 <= x <= 2^31 - 1
"""

# define an input for testing purposes
x = 1534236469

# actual code to submit
test = []

for i in str(x):
    test += i

for z in range(len(test)):
    if test[-1] == '0':
        test.pop(-1)
    else:
        break

if test == []:
    test.append('0')

if test[0] == '-':
    test.append('-')
    test.pop(0)

test.reverse()

solved = "".join(test)

# use print statement to check if it works
if int(solved) > -2147483648 and int(solved) < 2147483648:
    print(int(solved))
else:
    print(0)