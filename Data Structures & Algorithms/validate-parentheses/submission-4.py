class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) == 1 : 
            return False

        for i in range(len(s)):
            if s[i] == "(" or  s[i] == "{" or  s[i] == "[":
                stack.append(s[i])
            else :
                if stack:
                    current = stack.pop()
                    if current == "[" and s[i] != "]":
                        return False
                    elif current == "(" and s[i] != ")":
                        return False
                    elif current == "{" and s[i] != "}":
                        return False
                else :
                    return False

        return True if len(stack) == 0 else False
        
