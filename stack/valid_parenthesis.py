class Solution:
    def isValid(self, s: str) -> bool:
        # "" -> true
        # ")(" -> false
        # "[]" -> true
        # "(([]))" -> true
        # "{[}]" -> false

        pairs = {")" : "(", "]" : "[", "}" : "{"}
        stack = []


        for c in s:
            if c in pairs: #if closing bracket
                if not stack or stack[-1] != pairs[c]: #if the stack is empty or the opening bracket doesnt match the open bracket in stack
                    return False
                else:
                    stack.pop() #pair matches, can remove it
            else:
                stack.append(c) #if opening bracket add to stack

        return not stack #true if the stack is empty and all pairs are matched