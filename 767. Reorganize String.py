class Solution:
    def reorganizeString(self, s: str) -> str:
        from collections import Counter
        import heapq
        
        # Count the frequency of each character in the string
        char_count = Counter(s)
        
        # Create a max heap to store characters based on their frequency
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)
        
        # Initialize an empty result string
        result = []
        
        # While there are characters in the heap
        while len(max_heap) >= 2:
            # Pop the most frequent character
            count1, char1 = heapq.heappop(max_heap)
            # Pop the second most frequent character
            count2, char2 = heapq.heappop(max_heap)
            
            # Append the characters to the result string
            result.extend([char1, char2])
            
            # Decrement the counts and reinsert the characters if they're not depleted
            if count1 + 1 < 0:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(max_heap, (count2 + 1, char2))
        
        # If there's one character left in the heap, append it to the result
        if max_heap:
            count, char = heapq.heappop(max_heap)
            if count < -1:
                return ""  # Not possible to rearrange
            result.append(char)
        
        # Return the result as a string
        return ''.join(result)
