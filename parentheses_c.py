#https://leetcode.com/problems/longest-valid-parentheses/description/
"""
time: 80ms
algorithm: dinamic
dinamic: longest[i] stores the longest length of valid parentheses which is end at i.
s[i] == ‘(’ -> set longest[i] to 0
s[i] == ‘)’ -> 2 ways
    a) s[i-1] == ‘(’ ### situation: ...()
        longest[i] = longest[i-2] + 2
    b) s[i-1] == ‘)’ and s[i-longest[i-1]-1] == ‘(’ ### situation ...((...))
        longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]
"""
old_s = "()())"
new_s = "#" * 2 + old_s
longest = [0] * len(new_s)

for curr in range(2, len(new_s)):
    if new_s[curr] == '(': continue 
    if new_s[curr] == ')':
        if new_s[curr-1] == '(':
            longest[curr] = longest[curr-2] + 2
        if new_s[curr-1] == ')' and new_s[curr-longest[curr-1]-1] == '(':
            longest[curr] = longest[curr-1] + 2 + longest[curr-longest[curr-1]-2]

print(max(longest))
