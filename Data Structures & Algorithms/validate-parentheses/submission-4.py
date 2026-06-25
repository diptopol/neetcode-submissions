class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2 != 0):
            return False

        stack = []
        map = {')': '(', '}': '{', ']': '['}
        
        for ch in s:
            if ch in map:
                top = stack.pop() if stack else '#'

                if top != map[ch]:
                    return False
            else:
                stack.append(ch)    
        
        return not stack


