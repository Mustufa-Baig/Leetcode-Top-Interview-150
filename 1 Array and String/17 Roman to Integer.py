class Solution:
    def romanToInt(self, s: str) -> int:
        total=0
        N=len(s)
        i=0
        while i<N:
            this=0

            c=s[i]
            nc=None
            if i<N-1:
                nc=s[i+1]
            
            if c=='I':
                if nc=='V':
                    this=4
                    i+=1
                elif nc=='X':
                    this=9
                    i+=1
                else:
                    this=1
            elif c=='V':
                this=5
            elif c=='X':
                if nc=='L':
                    this=40
                    i+=1
                elif nc=='C':
                    this=90
                    i+=1
                else:
                    this=10
            elif c=='L':
                this=50
            elif c=='C':
                if nc=='D':
                    this=400
                    i+=1
                elif nc=='M':
                    this=900
                    i+=1
                else:
                    this=100
            elif c=="D":
                this=500
            elif c=="M":
                this=1000

            i+=1
            total+=this
        
        return total

