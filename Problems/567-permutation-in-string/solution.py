from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len2 < len1: return False

        letters = [0 for i in range(26)]
        scanner = [0 for i in range(26)]
        for i in range(len1):
            letters[self.getLetterIndex(s1[i])] += 1
            scanner[self.getLetterIndex(s2[i])] += 1
        if self.checkMatch(scanner, letters): return True

        for i in range(len1, len2):
            scanner[self.getLetterIndex(s2[i])] += 1
            scanner[self.getLetterIndex(s2[i - len1])] -= 1
            if self.checkMatch(scanner, letters): return True

        return False

    def checkMatch(self, source: List[int], target: List[int]) -> bool:
        return all(s == t for s, t in zip(source, target))

    def getLetterIndex(self, c: str) -> int:
        return ord(c) - ord("a")