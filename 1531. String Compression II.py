class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, k):
            if i >= len(s):
                return 0

            answer = math.inf
            # two basic cases
            if k > 0:
                # 1. remove char
                answer = min(answer, dp(i+1, k-1))
            # 2. add char
            answer = min(answer, 1+dp(i+1, k))
            
            # try all possible compressed substrings
            j = i + 1
            same = 1
            while j < len(s):
                if s[j] == s[i]:
                    same += 1
                # we can remove some chars for example in this case:
                # "aaaabbaaaa", if k >= 2 it will remove both "b"
                # and keep counting "a"
                elif k > 0:
                    k -= 1
                else:
                    break
                j += 1
                # in case of "aaaaaaaaa", same = 9
                # and len(str(same)) = 1 -> 9a -> 1 + 1,
                # in case  of "aaaaaaaaa", same = 10
                # and len(str(same)) = 2 -> 10a -> 2 + 1
                answer = min(answer, len(str(same))+1+dp(j, k))

            return answer
        
        return dp(0, k)
