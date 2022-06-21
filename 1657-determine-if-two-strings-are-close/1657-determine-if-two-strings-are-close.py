class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if Counter(word1).keys() != Counter(word2).keys():
            return False
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())