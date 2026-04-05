class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), key=lambda x: x[0])
        i = 0
        pq = []
        
        while k > 0:
            while i < len(projects) and projects[i][0] <= w:
                heappush(pq, -projects[i][1])
                i += 1
            
            if not pq:
                break
            
            w += -heappop(pq)
            k -= 1
        
        return w
