class Solution:
    def isValid(self, s: str) -> bool:
        close = {")":"(", "]":"[","}":"{"}

        stack = []

        for c in s:
            if c in close:
                if stack and stack[-1]==close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
