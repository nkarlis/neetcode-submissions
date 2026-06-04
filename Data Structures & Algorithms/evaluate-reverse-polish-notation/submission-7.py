class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        stack = []
        for t in tokens:
            if t == "+":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(temp1+temp2)
            elif t == "*":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(temp1*temp2)
            elif t == "-":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(temp2-temp1)
            elif t == "/":
                temp1, temp2 = stack.pop(), stack.pop()
                stack.append(int(float(temp2)/temp1))
            else:
                stack.append(int(t))
        return stack.pop()
            