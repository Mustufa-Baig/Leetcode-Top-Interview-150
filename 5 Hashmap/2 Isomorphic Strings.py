class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isoMap={}
        if len(s)!=len(t):
            return False
        N=len(s)
        for i in range(N):
            if s[i] in isoMap:
                if isoMap[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in isoMap.values():
                    return False
                isoMap[s[i]]=t[i]
        return True