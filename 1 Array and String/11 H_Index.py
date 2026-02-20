class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        N=len(citations)
        for i,n in enumerate(citations):
            if n+i>=N:
                return N-i
        return 0

