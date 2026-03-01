class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        anaMap={}
        for c in s:
            if c in anaMap:
                anaMap[c]+=1
            else:
                anaMap[c]=1
        for c in t:
            if not(c in anaMap) or anaMap[c]==0:
                return False
            anaMap[c]-=1
        return True


