class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res=0
        for word in words:
            for char in word:
                if chars.count(char)<word.count(char):
                    break
            else:
                res+=len(word)
        return res
