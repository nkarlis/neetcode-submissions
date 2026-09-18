class Solution:
    def intToRoman(self, num: int) -> str:
        valToSymbol = [
                [1000, "M"],
                [900, "CM"],
                [500 , "D"],
                [400 , "CD"],
                [100, "C"],
                [90, "XC"],
                [50, "L"],
                [40, "XL"],
                [10, "X"],
                [9, "IX"],
                [5, "V"],
                [4, "IV"],
                [1 , "I"]
        ]
        res = ""
        for val, sym in valToSymbol:
            count = num // val
            if count > 0:
                res += count * sym
                num %= val
        return res