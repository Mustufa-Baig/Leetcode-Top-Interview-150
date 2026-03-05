class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c.isdigit() or (c[0]=='-' and c[1:].isdigit()):
                stack.append(int(c))
            elif c in '+-*/':
                b=stack.pop()
                a=stack.pop()
                if c=='+':
                    stack.append(a+b)
                elif c=='-':
                    stack.append(a-b)
                elif c=='*':
                    stack.append(a*b)
                elif c=='/':
                    stack.append(int(a/b))
        return stack.pop()

        