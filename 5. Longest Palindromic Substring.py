class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        # Create a table to store the results of subproblems
        dp = [[False] * n for _ in range(n)]

        start = 0  # Initialize the start index of the longest palindromic substring
        max_len = 1  # Initialize the maximum length of the palindromic substring

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1  # Ending index of the current substring

                # Check if the current substring is a palindrome
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if length > max_len:
                        start = i
                        max_len = length

        return s[start:start + max_len]

# Example usage:
solution = Solution()
s = "babad"
result = solution.longestPalindrome(s)
print(result)  # Output: "bab" or "aba" is a valid answer
