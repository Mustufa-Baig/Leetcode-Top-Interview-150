class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        surplus = 0
        total_surplus = 0
        
        start = 0
        for i in range(N):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            
            if surplus < 0:
                surplus = 0
                start = i + 1

        if total_surplus < 0:
            return -1
        else:
            return start
