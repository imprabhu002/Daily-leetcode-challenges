class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len_s1, len_s2, len_s3 = len(s1), len(s2), len(s3)
        
        # If the lengths of s1 and s2 don't add up to the length of s3, it's impossible to interleave them.
        if len_s1 + len_s2 != len_s3:
            return False
        
        # Create a 2D DP table to store the results of subproblems.
        dp = [[False] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        
        # Base case: if both s1 and s2 are empty, then s3 is also empty and hence interleaving is possible.
        dp[0][0] = True
        
        # Fill the DP table based on whether characters of s1, s2, and s3 can be interleaved.
        for i in range(len_s1 + 1):
            for j in range(len_s2 + 1):
                if i > 0 and s1[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]
                if j > 0 and s2[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
        
        return dp[len_s1][len_s2]
