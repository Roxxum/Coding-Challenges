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
s = "(}{)"
#s = "{[]}"

# actual code to submit
def solution(input):
    pairs = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        ")" : None,
        "]" : None,
        "}" : None
    }
    ans = list(s)
    count = 0

    for i in ans[0:-1]:
        print(-ans.index(i)-1, 'is', ans[-ans.index(i) -1], ans[-ans.index(i)], 'is', -ans.index(i))
        print(-ans.index(i)-1, "<", (-len(ans) / 2))
        if ans[ans.index(i)+1] == pairs[i]:
            print(ans[ans.index(i)+1], 'pairs with', pairs[i])
            count += 2
        elif ans[-ans.index(i) -1] == pairs[i] and -ans.index(i) >= (-len(ans) / 2):
            print(ans[-ans.index(i) -1], 'pairs with', pairs[i], 'and', -ans.index(i)-1, "<", (-len(ans) / 2))
            count += 2

    if count == len(ans):
        return True
    else:
        return False
# use print statement to check if it works
print(solution(s))
