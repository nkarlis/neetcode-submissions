class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True  # Base case: empty suffix is valid

        # Iterate backwards
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                # 1. Check if word fits within remaining bounds
                # 2. Check if it matches
                # 3. Check if the rest of the string is already valid
                if (i + len(w) <= n) and s[i : i + len(w)] == w and dp[i + len(w)]:
                    dp[i] = True
                    # We can break the inner loop because we found at least
                    # one way to segment from i, making dp[i] True.
                    break
        return dp[0]