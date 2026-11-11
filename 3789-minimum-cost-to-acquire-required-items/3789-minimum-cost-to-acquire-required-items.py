class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        a = need1 * cost1 + need2 * cost2
        b = max(need1, need2) * costBoth

        m = min(need1, need2)
        c = m * costBoth + (need1 - m) * cost1 + (need2 - m) * cost2

        return min(a, b, c)