class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for i in range(len(s)):
            if s[i] not in brackets:
                stack.append(s[i])
            else:
                if len(stack) == 0 or stack.pop() != brackets[s[i]]:
                    return False
        return len(stack) == 0