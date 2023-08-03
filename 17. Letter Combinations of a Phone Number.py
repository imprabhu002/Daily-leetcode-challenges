class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        for i in range(len(digits)):
            letters = digit_to_letters[digits[i]]
            if i == 0:
                result = [letter for letter in letters]
            else:
                new_result = []
                for letter in letters:
                    for word in result:
                        new_result.append(word + letter)
                result = new_result
        return result
