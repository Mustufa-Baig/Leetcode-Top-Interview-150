class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        N=len(strs[0])
        prefix=''
        for i in range(1,N+1):
            pf=strs[0][:i]
            print(pf)
            for s in strs:
                if s[:i]!=pf:
                    return prefix
            prefix=pf

        return prefix
        

