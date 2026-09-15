class Solution:
    def romanToInt(self, s: str) -> int:
        SymbolToValue = {
            "I": 1,
            "IV": 5,
            "V": 5,
            "IX": 9,
            "X": 10,
            "LX": 40,
            "L": 50,
            "LC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and SymbolToValue[s[i]] < SymbolToValue[s[i + 1]]:
                res -= SymbolToValue[s[i]]
            else:
                res += SymbolToValue[s[i]]
        return res
       