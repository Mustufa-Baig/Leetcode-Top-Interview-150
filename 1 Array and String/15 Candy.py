class Solution:
    def candy(self, ratings: List[int]) -> int:
        N=len(ratings)
        candys=[1]*N
        for i in range(1,N):
            if ratings[i]>ratings[i-1]:
                candys[i]=candys[i-1]+1

        for i in reversed(range(N-1)):
            if ratings[i]>ratings[i+1]:
                if candys[i]<=candys[i+1]:
                    candys[i]=candys[i+1]+1
            
        return sum(candys)
