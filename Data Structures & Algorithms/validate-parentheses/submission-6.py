class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}  # closing → opening
        
        for char in s:
            if char in match:  # it's a closing bracket
                if not stack or stack.pop() != match[char]:
                    return False
            else:  # it's an opening bracket
                stack.append(char)
        
        return len(stack) == 0
            
