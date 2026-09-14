class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif i in brackets.keys():
                if not stack or stack.pop() != brackets[i]:
                    return False
        
        return len(stack) == 0