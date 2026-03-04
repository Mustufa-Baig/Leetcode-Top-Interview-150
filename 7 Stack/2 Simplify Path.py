class Solution:
    def simplifyPath(self, path: str) -> str:
        travel=[]
        for addr in path.split('/'):
            if addr:
                if addr=='..':
                    if travel:
                        travel.pop()
                else:
                    if not(addr=='.'):
                        travel.append(addr)
        return '/'+''.join([ p+'/' for p in travel ])[:-1]

