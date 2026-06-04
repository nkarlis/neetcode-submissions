class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == '+':
                x, y = stack.pop(), stack.pop()
                stack.append(x+y)
            elif t == '-':
                x, y = stack.pop(), stack.pop()
                stack.append(y-x)

            elif t == '*':
                x, y = stack.pop(), stack.pop()
                stack.append(x*y)
            
            elif t == '/':
                x, y = stack.pop(), stack.pop()
                stack.append(int(float(y)/x))
            else:
                stack.append(int(t))
        return stack.pop() if stack else 0