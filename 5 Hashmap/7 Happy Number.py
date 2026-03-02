class Solution:
    def isHappy(self, n: int) -> bool:
        num=n
        seen=[num]
        while True:
            num=sum([int(d)**2 for d in str(num)])
            if num==1:
                return True
            elif num in seen:
                return False
            else:
                seen.append(num)
