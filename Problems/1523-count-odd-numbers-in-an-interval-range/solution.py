class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low) // 2 + ((low % 2) | (high % 2))
