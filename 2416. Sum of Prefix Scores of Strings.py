class Node:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

class Solution:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.children[idx] is None:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            curr.count += 1

    def sumPrefixScores(self, words):
        for word in words:
            self.insert(word)

        ans = []
        for word in words:
            curr = self.root
            total_score = sum(curr.count for c in word if (curr := curr.children[ord(c) - ord('a')]) is not None)
            ans.append(total_score)

        return ans
