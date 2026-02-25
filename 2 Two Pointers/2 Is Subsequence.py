class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ref=0
        if len(s)>len(t):
            return False
        if not(s):
            return True
            
        for sample in t:
            if sample==s[ref]:
                ref+=1
                if ref==len(s):
                    return True
                
        return False
