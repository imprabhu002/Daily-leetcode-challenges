from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # Initialize a boolean array to store whether it is possible to segment s[i:n] into words from wordDict
        dp = [False] * (n + 1)
        dp[n] = True  # Empty string is always present in the dictionary

        # Traverse the input string from right to left
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                # Check if the word at index i is present in the dictionary and if we can segment the remaining string
                if i + len(word) <= n and s[i:i + len(word)] == word and dp[i + len(word)]:
                    dp[i] = True
                    break

        return dp[0]

# Example usage:
sol = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(sol.wordBreak(s, wordDict))  # Output: True
