class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        a = Counter(word1)
        b = Counter(word2)
        if a.keys() != b.keys():
            return False
        return sorted(a.values()) == sorted(b.values())