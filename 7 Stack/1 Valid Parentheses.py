class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not(stack):
                    return False
                top=stack[-1]
                if c==')' and top=='(':
                    stack.pop()
                elif c==']' and top=='[':
                    stack.pop()
                elif c=='}' and top=='{':
                    stack.pop()
                else:
                    return False
        
        return False if stack else True
