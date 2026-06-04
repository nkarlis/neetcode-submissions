class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
         # store the previous temperatures with index
        stack = []# pair (temp, index)

        for i, t in enumerate(temperatures):
            # is stack not empty, and check if current temp is grater than the top temp
            while stack and stack[-1][0] < t:
                stackTemp, stackIndex= stack.pop()
                res[stackIndex] = i - stackIndex

            stack.append((t, i))


        return res