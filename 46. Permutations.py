from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                # Swap the elements to create a permutation
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recursively generate permutations with the updated array
                backtrack(start + 1)
                
                # Backtrack and restore the original order of elements
                nums[start], nums[i] = nums[i], nums[start]
        
        result = []
        backtrack(0)
        return result

# Example usage:
nums = [1, 2, 3]
solution = Solution()
permutations = solution.permute(nums)
print(permutations)
