class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort the pairs based on their second value (right end)
        pairs.sort(key=lambda x: x[1])
        
        n = len(pairs)
        dp = [1] * n  # Initialize dp array with 1 since every pair is at least a chain of length 1
        
        for i in range(1, n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
