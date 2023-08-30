class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        res = 0
        for x in nums[::-1]:
            temp = (x-1)//last
            res += temp
            last = x//(temp+1)

        return res
