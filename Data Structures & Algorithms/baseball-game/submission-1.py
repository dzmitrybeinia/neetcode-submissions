class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            n = len(stack)
            if op == "+":
                prev = int(stack[n - 1])
                prev_prev = int(stack[n - 2])
                stack.append(prev + prev_prev)
            elif op == "C":
                stack.pop()
            elif op == "D":
                prev = int(stack[n - 1])
                stack.append(prev * 2)
            else:
                stack.append(int(op))
        return sum(stack)
