class Solution:
    def isValid(self, s: str) -> bool:

        brackets = {
            ']':'[',
            '}':'{',
            ')':'('
        }

        stack = []

        for bracket in s:
            if bracket in '[({':
                stack.append(bracket)
            else:
                if len(stack) == 0 or brackets[bracket] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
