class Solution:
    VALUE_MAP = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s: str) -> int:
        total = 0

        for c in s:
            total += self.VALUE_MAP[c]

        if "IV" in s or "IX" in s: total -= 2
        if "XL" in s or "XC" in s: total -= 20
        if "CD" in s or "CM" in s: total -= 200

        return total