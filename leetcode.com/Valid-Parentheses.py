"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true


Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

# define an input for testing purposes
s = "([)]"

# actual code to submit
def solution(input):
    pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{"}

    door = {
        "(" : "Open",
        "[" : "Open",
        "{" : "Open",
        ")" : "Closed",
        "]" : "Closed",
        "}" : "Closed"}

    slist = list(s)
    check = []

    for i in slist:
        if door[i] == "Open":
            check.append(i)
        elif door[i] == "Closed" and len(check) > 0:
            if pairs[i] == check[-1]:
                check.pop()
            else:
                check.insert(0, i)
        else:
            check.insert(0, i)

    if len(check) == 0:
        return True
    else:
        return False

# use print statement to check if it works
print(solution(s))
