class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid='abcdefghijklmnopqrstuvwxyz0123456789'
        modified=''.join([c for c in s.lower() if c in valid])
        
        rP=len(modified)-1
        for lP in modified:
            if lP!=modified[rP]:
                return False
            rP-=1
        return True
