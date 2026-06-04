class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # 0... to amount
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    # 1 from c the current coin we use
                    # dp[a-c] amount 12 - coin 10 then dp[2]
                    dp[a] = min(dp[a], 1 + dp[a-c])
                else:
                    break

        return dp[amount] if dp[amount] != amount+1 else -1