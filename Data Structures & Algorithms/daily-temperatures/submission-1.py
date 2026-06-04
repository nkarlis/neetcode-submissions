class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # index, temp
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]:
                sindex, t = stack.pop()
                res[sindex] = i-sindex
            
            stack.append((i, temperatures[i]))


        return res