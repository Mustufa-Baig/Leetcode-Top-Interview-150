class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        longest=0
        subs=""
        for end,c in enumerate(s):
            if not(c in subs):
                subs+=c
            else:
                if (end-start) > longest:
                    longest=end-start
                
                shift=subs.index(c)+1
                start+=shift
                subs=subs[shift:]+c
                

        if len(subs)>longest:
            return len(subs)
        return longest
