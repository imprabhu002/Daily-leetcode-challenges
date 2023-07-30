import functools
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4500:
            return 1.0
        
        @cache
        def prob(a,b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0

            return 1/4 * (prob(a-100,b) + prob(a-75,b-25) + prob(a-50,b-50) + prob(a-25,b-75))

        return prob(n,n)
