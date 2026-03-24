from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0
        
        bank_set = set(bank)
        char_set = {'A', 'C', 'G', 'T'}
        
        level = 0
        visited = set()
        queue = deque([startGene])
        visited.add(startGene)
        
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == endGene:
                    return level
                
                for i in range(len(curr)):
                    for c in char_set:
                        next_gene = curr[:i] + c + curr[i+1:]
                        if next_gene in bank_set and next_gene not in visited:
                            queue.append(next_gene)
                            visited.add(next_gene)
            level += 1
        
        return -1
