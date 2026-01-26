class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost: return 0

        curr = 0
        a, b = cost[0], cost[1]

        for i in range(2, len(cost)):
            curr = cost[i] + min(a, b)
            a = b
            b = curr
        
        return min(a, b)