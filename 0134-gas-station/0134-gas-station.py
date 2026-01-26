class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        c_gas, start = 0, 0
        for i in range(len(gas)):
            c_gas += gas[i] - cost[i]
            if c_gas < 0:
                c_gas = 0
                start = i + 1
        
        return start