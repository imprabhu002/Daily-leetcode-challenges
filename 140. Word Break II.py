class Solution:
    def __init__(self):
        self.words = set()
        self.sentences = []

    def backtrack(self, s, i0, i1, spaces):
        if i1 >= len(s):
            if s[i0:i1] in self.words:
                sen = []
                for i in range(len(s)):
                    sen.append(s[i])
                    if spaces[i]:
                        sen.append(" ")
                self.sentences.append("".join(sen))
            return

        if s[i0:i1 + 1] in self.words:
            spaces[i1] = True
            self.backtrack(s, i1 + 1, i1 + 1, spaces)
            spaces[i1] = False

        self.backtrack(s, i0, i1 + 1, spaces)

    def wordBreak(self, s, wordDict):
        self.sentences = []
        self.words = set(wordDict)
        self.backtrack(s, 0, 0, [False] * len(s))
        return self.sentences
