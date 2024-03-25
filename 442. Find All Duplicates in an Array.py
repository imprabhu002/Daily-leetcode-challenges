class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp = set()
        out = []
        for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                out.append(i)
        return out
