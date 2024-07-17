class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True

        stack = []
        bracket_mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            print(stack)
            if char in bracket_mapping:
                if stack and stack[-1] == bracket_mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return not stack

solution = Solution()
print(solution.isValid("()"))      # Output: True
print(solution.isValid("()[]{}"))  # Output: True
print(solution.isValid("(]"))      # Output: False
print(solution.isValid("([)]"))    # Output: False
print(solution.isValid("{[]}"))    # Output: True

