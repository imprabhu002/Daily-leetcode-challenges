class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        # Try all possible substring lengths
        for length in range(1, n // 2 + 1):
            if n % length == 0:  # Check if length is a divisor of n
                substring = s[:length]  # Get the potential substring
                
                # Construct the full string by repeating the substring
                constructed = substring * (n // length)
                
                if constructed == s:  # If constructed string matches the input string
                    return True
        
        return False
