class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        isoMap={}
        sL=s.split()
        N=len(sL)
        if N!=len(pattern):
            return False
        
        for i in range(N):
            if sL[i] in isoMap:
                if isoMap[sL[i]]!=pattern[i]:
                    return False
            else:
                if pattern[i] in isoMap.values():
                    return False
                isoMap[sL[i]]=pattern[i]
        return True


