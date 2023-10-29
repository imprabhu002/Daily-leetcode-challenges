class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        base = minutesToTest // minutesToDie + 1
        
        min_pigs = 0
        while (base ** min_pigs) < buckets:
            min_pigs += 1
        
        return min_pigs
