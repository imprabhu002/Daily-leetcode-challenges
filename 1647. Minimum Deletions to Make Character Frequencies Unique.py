class Solution:
    def minDeletions(self, s: str) -> int:
        # Step 1: Count the frequency of each character
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Step 2: Create a set to track encountered frequencies
        encountered_freq = set()

        # Step 3: Initialize the deletions counter
        deletions = 0

        # Step 4: Iterate through frequencies
        for freq in char_count.values():
            while freq in encountered_freq:
                # Decrement the frequency until it's not in the set
                freq -= 1
                deletions += 1
            if freq > 0:
                # Mark the current frequency as encountered
                encountered_freq.add(freq)

        # Step 6: Return the total number of deletions
        return deletions

# Example usage:
solution = Solution()
s = "aaabbbccc"
result = solution.minDeletions(s)
print(result)  
