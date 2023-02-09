from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        slen, plen = len(s), len(p)
        if slen < plen: return []

        res = []
        target_fingerprint = self.getFingerprint(p)
        curr_fingerprint = self.getFingerprint(s[:plen])
        for i in range(slen - plen + 1):
            if i > 0:
                curr_fingerprint[ord(s[i - 1]) - ord('a')] -= 1
                curr_fingerprint[ord(s[i + plen - 1]) - ord('a')] += 1
            if self.isAnagram(curr_fingerprint, target_fingerprint):
                res.append(i)

        return res

    def getFingerprint(self, s: str) -> List[int]:
        fingerprint = [0 for _ in range(26)]

        for c in s:
            fingerprint[ord(c) - ord('a')] += 1

        return fingerprint
    
    def isAnagram(self, fingerprint1: List[int], fingerprint2: List[int]) -> bool:
        return all(c1 == c2 for c1, c2 in zip(fingerprint1, fingerprint2))