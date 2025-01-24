class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to map closing brackets to their corresponding opening brackets
        valid_bracket = {')': '(', '}': '{', ']': '['}
        stack = []  # Stack to keep track of open brackets

        for c in s:
            if c in valid_bracket:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Use '#' as a dummy value for empty stack
                if valid_bracket[c] != top_element:  # Check if the brackets match
                    return False
            else:
                stack.append(c)  # Push opening brackets onto the stack

        return not stack  # Return True if the stack is empty, False otherwise


solution = Solution()
print(solution.isValid("["))
