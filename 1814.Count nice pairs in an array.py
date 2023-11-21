from collections import Counter
from typing import List

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        
        def rev(x):
            return int(str(x)[::-1])
        
        diff_count = Counter(num - rev(num) for num in nums)
        
        nice_pairs = 0
        
        for count in diff_count.values():
            nice_pairs = (nice_pairs + count * (count - 1) // 2) % mod
        
        return nice_pairs

nums = [42, 11, 1, 97]
solution = Solution()
result = solution.countNicePairs(nums)
print(result)
