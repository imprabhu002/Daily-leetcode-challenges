class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        prabhu = 0

        i = 0
        j = len(tokens) - 1

        while i<=j:
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
                prabhu = max(prabhu, score)
            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return prabhu
