class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        canvas=''
        N=len(s)
        g=2*(numRows-1)
        for i in range(numRows):
            for j in range(i,N,g):
                canvas+=s[j]
                if i>0 and i<numRows-1 and j+g-2*i<N:
                    canvas+=s[j+g-2*i]
        return canvas
