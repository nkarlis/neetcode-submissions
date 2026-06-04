class Solution:
    def isValid(self, s: str) -> bool:
        close = {")":"(", "]":"[", "}":"{"}
        stack = []

        for c in s:
            if c in close and stack:
                if stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False    
