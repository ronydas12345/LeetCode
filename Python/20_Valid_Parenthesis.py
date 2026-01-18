class Solution:
    def isValid(self, s: str) -> bool:
        left, right, stack = ["(", "[", "{"], [")", "]", "}"], []
        for i in range(len(s)):
            if s[i] in left:
                stack.append(s[i])
            elif stack and left.index(stack[len(stack) - 1]) == right.index(s[i]):
                stack.pop()
            else:
                return False
        return stack == []

