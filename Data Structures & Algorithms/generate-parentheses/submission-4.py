class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []
        def dfs(openN, closedN):
            if n == openN == closedN:
                res.append("".join(stack))
                return
            if n > openN:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()
            if openN > closedN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()
        dfs(0, 0)
        return res