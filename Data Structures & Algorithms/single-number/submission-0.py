class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        dupl = {}

        for num in nums:
            dupl[num] = dupl.get(num, 0) + 1
        
        for num, val in dupl.items():
            if val == 1:
                return num