from typing import List

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for e in nums[1:]:
            prefix.append(prefix[-1] + e)

        res = [((e * idx) - (prefix[idx - 1] if idx != 0 else 0)) + ((prefix[-1] - prefix[idx]) - (e * (len(nums) - idx - 1)) if idx != len(nums) - 1 else 0) for idx, e in enumerate(nums)]
        
        return res
