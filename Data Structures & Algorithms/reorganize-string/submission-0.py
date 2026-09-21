class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        # Sort characters by frequency in descending order
        sorted_chars = sorted(count.keys(), key=lambda x: -count[x])
        
        # Check if the most frequent character exceeds 
        # the maximum allowed limit
        if count[sorted_chars[0]] > (n + 1) // 2:
            return ""
            
        res = [''] * n
        idx = 0
        
        # Place characters greedily
        for char in sorted_chars:
            freq = count[char]
            for _ in range(freq):
                res[idx] = char
                idx += 2
                # Once we reach or exceed the end of the 
                # array, switch to odd indices
                if idx >= n:
                    idx = 1
                    
        return "".join(res)
        