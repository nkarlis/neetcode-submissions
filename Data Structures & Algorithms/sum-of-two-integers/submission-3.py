class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff

        # while carry is not 0, we have a carry
        while b != 0:
            # carry
            tmp = (a & b) << 1
            #(~x = -x-1)
            # xor to calculate the sum without carry
            a = (a ^ b) & mask
            b = tmp & mask

        if a > mask // 2:
            return ~(a ^ mask)
        else:
            return a
            