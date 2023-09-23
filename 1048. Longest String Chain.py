class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort the words by length in ascending order
        words.sort(key=len)
        
        # Create a dictionary to store the longest chain for each word
        longest_chain = {}
        
        # Initialize the longest chain for each word to be 1
        for word in words:
            longest_chain[word] = 1
        
        # Iterate through each word
        for word in words:
            # Try removing one character from the word at each position
            for i in range(len(word)):
                prev_word = word[:i] + word[i+1:]
                
                # If the previous word is in the dictionary, update the longest chain
                if prev_word in longest_chain:
                    longest_chain[word] = max(longest_chain[word], longest_chain[prev_word] + 1)
        
        # Find the maximum chain length
        max_chain = max(longest_chain.values())
        
        return max_chain

# Example usage:
solution = Solution()
words = ["a", "b", "ba", "bca", "bda", "bdca"]
print(solution.longestStrChain(words))
