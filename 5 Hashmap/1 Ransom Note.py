class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag={}
        for c in magazine:
            if c in mag:
                mag[c]+=1
            else:
                mag[c]=1
        for c in ransomNote:
            if c in mag and mag[c]>0:
                mag[c]-=1
            else:
                return False
        return True

