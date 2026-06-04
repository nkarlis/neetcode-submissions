class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                t1, t2 = stack.pop(), stack.pop()
                stack.append(t1 + t2)
            elif t == "*":
                t1, t2 = stack.pop(), stack.pop()
                stack.append(t1 * t2)
            elif t == "-":
                t1, t2 = stack.pop(), stack.pop()
                stack.append(t2 - t1)
            elif t == "/":
                t1, t2 = stack.pop(), stack.pop()
                stack.append(int(float(t2)/t1))
            else:
                stack.append(int(t))

        return stack[0] if stack else 0