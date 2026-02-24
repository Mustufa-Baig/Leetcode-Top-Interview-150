class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        N=len(needle)
        H=len(haystack)
        if H==N:
            if needle==haystack:
                return 0
            return -1

        for i in range(H-N+1):
            if haystack[i:N+i]==needle:
                return i
        return -1

