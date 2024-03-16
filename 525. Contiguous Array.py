class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0: -1}
        max_length = 0
        count = 0
        
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            
            if count in hashmap:
    
                max_length = max(max_length, i - hashmap[count])
            else:
                hashmap[count] = i
        
        return max_length
