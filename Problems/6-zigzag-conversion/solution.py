class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s

        l = len(s)
        t = 2 * numRows - 2
        res = []

        for i in range(numRows):
            for j in range(l // t + 1):
                if j * t + i < l:
                    res.append(s[j * t + i])
                if not i in (0, numRows - 1) and j * t + t - i < l:
                    res.append(s[j * t + t - i])

        return "".join(res)
