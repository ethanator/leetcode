from typing import List


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2): return False

        sim = {}
        for pair in similarPairs:
            if not pair[0] in sim:
                sim[pair[0]] = []
            sim[pair[0]].append(pair[1])

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2: continue
            if word1 in sim and word2 in sim[word1]: continue
            if word2 in sim and word1 in sim[word2]: continue
            return False

        return True
