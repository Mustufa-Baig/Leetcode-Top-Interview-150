class Solution:
    def isAna(self,s,t):
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=[[strs[0]]]

        for s in strs[1:]:
            for g in groups:
                if self.isAna(s,g[0]):
                    g.append(s)
                    break
            else:
                groups.append([s])
        return groups
                
